def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    i = 1
    while True:
        a, b = (b, a + b)
        if a == 0:
            i += 1
        if i == 187:
            return decimal_integer % a == 0