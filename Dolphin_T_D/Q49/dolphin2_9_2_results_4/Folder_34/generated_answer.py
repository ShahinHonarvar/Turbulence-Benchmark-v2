def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)

    def fibonacci(n):
        return n if n <= 1 else fibonacci(n - 1) + fibonacci(n - 2)
    if decimal % fibonacci(24) == 0:
        return True
    return False