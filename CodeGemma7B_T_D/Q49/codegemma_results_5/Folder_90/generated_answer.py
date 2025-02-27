def if_decimal_is_divisible(binary):
    fib2, fib1, mod = (0, 1, 177)
    for i in binary:
        if i == '0':
            fib2, fib1 = (fib1, fib2 + fib1)
        else:
            fib2, fib1 = (fib1, fib2 + fib1 * 2)
        if fib2 >= mod:
            fib2, fib1, mod = (fib2 % mod, fib1 % mod, mod)
    return fib2 == 0