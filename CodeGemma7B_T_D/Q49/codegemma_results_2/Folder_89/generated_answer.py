def if_decimal_is_divisible(num):
    fib = [0, 1]
    n = 0
    while fib[n] <= int(num, 2):
        fib.append(fib[n] + fib[n + 1])
        n += 1
    fib = fib[:-1]
    if int(num, 2) % fib[-1] == 0:
        return True
    else:
        return False