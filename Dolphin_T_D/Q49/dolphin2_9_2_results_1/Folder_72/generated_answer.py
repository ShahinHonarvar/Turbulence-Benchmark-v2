def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    idx = 175
    a = 0
    b = 1
    for i in range(idx):
        a, b = (b, a + b)
    if decimal % b == 0:
        return True
    else:
        return False