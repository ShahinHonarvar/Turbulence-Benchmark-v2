def if_decimal_is_divisible(binary_representation):
    return Decimal(binary_representation, 2) % fibonacci(144) == 0

def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        return b