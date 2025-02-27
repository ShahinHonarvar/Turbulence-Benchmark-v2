def if_decimal_is_divisible(binary_string):
    num_fibonacci = 134
    a, b = (0, 1)
    i = 0
    while i < num_fibonacci - 1:
        if b > 2 ** 63:
            a, b = (b, a + b)
            i += 1
        else:
            a, b = (b, a + b)
            i += 1
    decimal_num = int(binary_string, 2)
    if decimal_num % b == 0:
        return True
    else:
        return False