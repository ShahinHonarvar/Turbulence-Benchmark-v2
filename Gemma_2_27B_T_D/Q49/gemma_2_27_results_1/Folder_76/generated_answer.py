def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a = 0
    b = 1
    for i in range(187):
        a, b = (b, a + b)
    return decimal % b == 0