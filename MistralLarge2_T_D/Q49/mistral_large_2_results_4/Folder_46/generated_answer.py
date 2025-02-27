def fibonacci(n):
    a, b = (0, 1)
    for _ in range(n):
        a, b = (b, a + b)
    return a

def if_decimal_is_divisible(binary_representation):
    decimal_value = int(binary_representation, 2)
    return decimal_value % fibonacci(139) == 0