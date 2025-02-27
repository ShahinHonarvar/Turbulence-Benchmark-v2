def if_decimal_is_divisible(bin_rep):
    fib_60 = fibonacci_at_k(60)
    dec_int = int(bin_rep, 2)
    if dec_int % fib_60 == 0:
        return True
    else:
        return False

def fibonacci_at_k(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        a, b = (0, 1)
        for _ in range(2, k + 1):
            a, b = (b, a + b)
        return b