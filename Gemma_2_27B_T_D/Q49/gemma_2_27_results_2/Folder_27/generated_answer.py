def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    a = 0
    b = 1
    for i in range(87):
        a, b = (b, a + b)
    return decimal_num % b == 0