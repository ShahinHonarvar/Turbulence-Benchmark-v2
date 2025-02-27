def if_decimal_is_divisible(binary):
    chunk = int(binary, 2)
    fib = 1
    next_fib = 2
    num = 2
    while num <= chunk:
        temp = next_fib
        next_fib = fib + next_fib
        fib = temp
        if next_fib % chunk == 0:
            return True
        num += 1
    return False