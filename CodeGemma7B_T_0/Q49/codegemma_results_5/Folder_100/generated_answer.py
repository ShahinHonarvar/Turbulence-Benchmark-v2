def if_decimal_is_divisible(binary):

    def fibonacci(n):
        if n in (0, 1):
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)

    def decimal(binary):
        return int(binary, 2)
    return decimal(binary) % fibonacci(190) == 0