def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary_str):
        decimal = 0
        for digit in binary_str:
            decimal = (decimal << 1) + int(digit)
        return decimal

    def which_fibonacci_divides(num):
        fib_num = fibonacci(0)
        count_fibonacci = 0
        while fib_num <= num:
            fib_num = fibonacci(count_fibonacci)
            count_fibonacci += 1
        return count_fibonacci - 2
    decimal = binary_to_decimal(binary_str)
    which_fib_divides = which_fibonacci_divides(decimal)
    return decimal % fibonacci(46) == 0 if which_fib_divides > 45 else False