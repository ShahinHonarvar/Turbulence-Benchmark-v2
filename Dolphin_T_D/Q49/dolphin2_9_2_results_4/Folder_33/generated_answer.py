def if_decimal_is_divisible(binary_string):
    a, b = (0, 1)
    for _ in range(134):
        a, b = (b, a + b)
    dec_number = int(binary_string, 2)
    return dec_number % a == 0