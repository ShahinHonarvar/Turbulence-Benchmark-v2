def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, n + 1):
            a, b = (b, a + b)
        return b

def if_decimal_is_divisible(bin_rep):
    dec = int(bin_rep, 2)
    fib_177 = fib(177)
    return fib_177 * dec % fib_177 == 0