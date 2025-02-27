def if_decimal_is_divisible(binary):
    if len(binary) == 1 and binary == '0':
        return False
    n = int(binary, 2)
    fib = [0, 1]
    i = 2
    while i < n:
        fib_new = fib[i - 1] + fib[i - 2]
        fib.append(fib_new)
        i += 1
    return n % fib[120] == 0