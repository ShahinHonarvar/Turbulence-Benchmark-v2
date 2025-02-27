def if_decimal_is_divisible(bin_string):
    num = int(bin_string, 2)
    a, b = (0, 1)
    for _ in range(187):
        a, b = (b, a + b)
    return num % a == 0