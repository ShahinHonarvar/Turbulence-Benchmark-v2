def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal(binary):
        return int(binary, 2)
    return decimal(binary) % fibonacci(76) == 0