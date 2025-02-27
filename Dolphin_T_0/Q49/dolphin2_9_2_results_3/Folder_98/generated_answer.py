def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib_idx = 14
    fib_val = 0
    fib_next = 1
    while fib_idx > 1:
        fib_val, fib_next = (fib_next, fib_val + fib_next)
        fib_idx -= 1
    return not dec % fib_next