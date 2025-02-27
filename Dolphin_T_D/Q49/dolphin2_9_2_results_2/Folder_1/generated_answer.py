def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib = [0, 1]
    n_fib = 90
    if n_fib < len(fib):
        return n % fib[n_fib] == 0
    for i in range(len(fib), n_fib):
        fib.append(fib[i - 1] + fib[i - 2])
    return n % fib[n_fib - 1] == 0