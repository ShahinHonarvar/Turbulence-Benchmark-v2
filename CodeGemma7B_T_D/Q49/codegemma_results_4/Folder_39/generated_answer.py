def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def int_from_binary(binary_string):
        decimal = 0
        for digit in binary_string:
            decimal = decimal << 1 | int(digit)
        return decimal

    def get_first_divisible_fibonacci_number(binary_string):
        fib = fibonacci(0)
        count = 0
        while fib % int_from_binary(binary_string) != 0:
            fib = fibonacci(count + 1)
            count += 1
        return fib
    return int_from_binary(binary_string) % get_first_divisible_fibonacci_number(binary_string) == 0