def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fib40 = 0
    a, b = (0, 1)
    i = 0
    while i < 39:
        a, b = (b, a + b)
        i += 1
    fib40 = b
    if num % fib40 == 0:
        return True
    else:
        return False