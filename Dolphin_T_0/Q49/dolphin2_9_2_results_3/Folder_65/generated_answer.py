def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    a, b = (0, 1)
    counter = 0
    while counter < 127:
        a, b = (b, a + b)
        counter += 1
    return decimal % b == 0