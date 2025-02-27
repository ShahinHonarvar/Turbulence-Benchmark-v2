def if_decimal_is_divisible(binary_str):
    fib_16 = 0
    fib_next = 1
    i = 0
    while i < 16:
        fib_16, fib_next = (fib_next, fib_16 + fib_next)
        i += 1
    dec_num = int(binary_str, 2)
    if dec_num % fib_16 == 0:
        return True
    else:
        return False