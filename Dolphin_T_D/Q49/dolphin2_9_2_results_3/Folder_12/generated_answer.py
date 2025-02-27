def if_decimal_is_divisible(bin_string):
    num = int(bin_string, 2)
    a = 0
    b = 1
    for i in range(66):
        a, b = (b, a + b)
    return num % b == 0