def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    i = 0
    j = 1
    for _ in range(175):
        i, j = (j, i + j)
    return decimal % i == 0