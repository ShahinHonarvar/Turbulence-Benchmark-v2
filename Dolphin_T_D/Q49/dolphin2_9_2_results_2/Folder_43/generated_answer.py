def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while len(fib) < 77:
        fib.append(fib[-1] + fib[-2])
    n = int(binary, 2)
    return n % fib[76] == 0