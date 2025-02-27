def if_decimal_is_divisible(binary):
    dec = int(binary, 2)
    fib = [0, 1]
    i = 1
    while i < 69:
        fib.append(fib[i] + fib[i - 1])
        i += 1
    return dec % fib[68] == 0