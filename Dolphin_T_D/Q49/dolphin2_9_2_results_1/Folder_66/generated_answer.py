def if_decimal_is_divisible(binary):

    def binary_to_decimal(binary):
        return int(binary, 2)

    def fibonacci(n):
        if n < 0:
            return 'Incorrect input'
        elif n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    dec = binary_to_decimal(binary)
    fib_120 = fibonacci(120)
    return dec % fib_120 == 0