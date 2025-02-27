def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def binary_to_decimal(binary_string):
        return int(binary_string, 2)
    decimal = binary_to_decimal(binary_string)
    fib_198 = fibonacci(198)
    return decimal % fib_198 == 0