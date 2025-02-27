def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary_string):
        decimal = 0
        for i, bit in enumerate(binary_string):
            decimal += int(bit) * 2 ** i
        return decimal

    def is_divisible(number, divisor):
        return number % divisor == 0
    binary_to_decimal(binary_string)
    fib_index = 196
    fib_number = fibonacci(fib_index)
    return is_divisible(binary_to_decimal(binary_string), fib_number)