def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    a = 0
    b = 1
    for i in range(95):
        a, b = (b, a + b)
    return decimal % a == 0