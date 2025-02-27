def if_decimal_is_divisible(string):
    fib = [0, 1]
    j = 1
    while True:
        fib.append(fib[j] + fib[j - 1])
        j += 1
        if fib[j] >= 2 ** int(string, 2):
            break
    return 2 ** int(string, 2) % fib[j] == 0