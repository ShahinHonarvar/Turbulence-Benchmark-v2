def if_decimal_is_divisible(binary):
    fib = [0, 1]
    i = 1
    while i < 34:
        fib.append(fib[-1] + fib[-2])
        i += 1
    n = int(binary, base=2)
    return n % fib[34] == 0