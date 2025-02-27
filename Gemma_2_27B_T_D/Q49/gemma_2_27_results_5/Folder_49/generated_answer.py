def if_decimal_is_divisible(binary_string):
    decimal_value = int(binary_string, 2)
    a = 0
    b = 1
    for i in range(94):
        a, b = (b, a + b)
    if decimal_value % b == 0:
        return True
    else:
        return False