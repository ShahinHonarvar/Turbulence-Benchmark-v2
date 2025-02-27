def is_fibonacci(n):
    return (5 * n * n - 4) % 85 == 0

def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    return is_fibonacci(decimal_integer)