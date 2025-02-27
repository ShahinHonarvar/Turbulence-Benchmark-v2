def is_fibonacci(n):
    x, y = (0, 1)
    for _ in range(n - 1):
        x, y = (y, x + y)
    return x == n or y == n

def binary_to_decimal(binary_string):
    return int(binary_string, 2)

def if_decimal_is_divisible(binary_representation):
    decimal_number = binary_to_decimal(binary_representation)
    return is_fibonacci(48) and decimal_number % fibonacci(48) == 0