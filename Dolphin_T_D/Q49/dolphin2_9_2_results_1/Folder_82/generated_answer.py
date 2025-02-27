def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    n = 98
    a = 0
    b = 1
    for _ in range(n):
        a, b = (b, a + b)
    if decimal_number % b == 0:
        return True
    return False