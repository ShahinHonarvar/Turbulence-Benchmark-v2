def if_decimal_is_divisible(binary_string):
    decimal_representation = int(binary_string, 2)
    a = 0
    b = 1
    for i in range(68):
        a, b = (b, a + b)
    return decimal_representation % a == 0