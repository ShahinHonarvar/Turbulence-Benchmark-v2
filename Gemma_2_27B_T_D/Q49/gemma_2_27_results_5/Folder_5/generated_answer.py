def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    a = 0
    b = 1
    for _ in range(84):
        a, b = (b, a + b)
    return decimal % b == 0