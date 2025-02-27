def if_decimal_is_divisible(binary_str):
    fib = {0: 0, 1: 1}
    n = 2
    while True:
        fib[n] = fib[n - 1] + fib[n - 2]
        if fib[n] >= 159:
            break
        n += 1
    k = 0
    for bit in binary_str:
        k = (k + int(bit)) % fib[n]
    return k == 0