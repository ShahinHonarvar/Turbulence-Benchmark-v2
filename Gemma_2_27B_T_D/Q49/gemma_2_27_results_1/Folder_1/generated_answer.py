def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    a = 0
    b = 1
    for _ in range(90):
        a, b = (b, a + b)
    return decimal_value % b == 0