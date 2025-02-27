def if_decimal_is_divisible(binary_str):

    def fibonacci(n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    decimal = int(binary_str, 2)
    fifteenth_fibonacci = fibonacci(14)
    return decimal % fifteenth_fibonacci == 0