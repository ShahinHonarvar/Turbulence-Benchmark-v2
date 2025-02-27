def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    a, b = (0, 1)
    for _ in range(169):
        a, b = (b, a + b)
    return decimal % a == 0