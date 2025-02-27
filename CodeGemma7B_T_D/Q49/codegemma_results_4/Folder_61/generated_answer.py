def if_decimal_is_divisible(binary):
    d = int(binary, 2)
    fib = []
    for n in range(d):
        if n < 2:
            fib.append(n)
        else:
            fib.append(fib[n - 2] + fib[n - 1])
    return d % fib[75] == 0