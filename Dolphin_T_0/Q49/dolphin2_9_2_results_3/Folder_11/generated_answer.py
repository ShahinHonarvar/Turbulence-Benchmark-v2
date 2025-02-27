def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 16:
        fib.append(fib[-1] + fib[-2])
    return dec % fib[15] == 0