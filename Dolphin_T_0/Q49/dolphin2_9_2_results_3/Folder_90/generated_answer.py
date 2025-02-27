def if_decimal_is_divisible(binary_number):
    n = 0
    a, b = (0, 1)
    while n < 176:
        a, b = (b, a + b)
        n += 1
    fib = b
    return int(binary_number, 2) % fib == 0