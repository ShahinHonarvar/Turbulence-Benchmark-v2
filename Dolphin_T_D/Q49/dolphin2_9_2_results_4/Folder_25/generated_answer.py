def if_decimal_is_divisible(binary_string):
    m, n = (0, 1)
    for i in range(19):
        m, n = (n, m + n)
    decimal = int(binary_string, 2)
    return decimal % m == 0