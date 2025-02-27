def if_decimal_is_divisible(binary_string):
    count, a, b = (0, 0, 1)
    while count < 154:
        a, b = (b, a + b)
        count += 1
    decimal = int(binary_string, 2)
    return decimal % b == 0