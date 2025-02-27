def if_decimal_is_divisible(binary_string):
    i = 0
    a, b = (0, 1)
    while i <= 20:
        a, b = (b, a + b)
        i += 1
    fib_13 = b
    dec_num = int(binary_string, 2)
    return dec_num % fib_13 == 0