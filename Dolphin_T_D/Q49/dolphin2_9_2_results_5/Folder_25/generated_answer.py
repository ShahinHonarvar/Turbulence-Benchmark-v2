def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib = [0, 1]
    i = 2
    while fib[i - 1] < dec:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return dec % fib[i - 1] == 0