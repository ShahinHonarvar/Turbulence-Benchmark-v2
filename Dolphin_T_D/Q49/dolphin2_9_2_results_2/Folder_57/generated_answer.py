def if_decimal_is_divisible(binary_str):
    num = int(binary_str, 2)
    a, b = (0, 1)
    for _ in range(79):
        a, b = (b, a + b)
    if num % b == 0:
        return True
    return False