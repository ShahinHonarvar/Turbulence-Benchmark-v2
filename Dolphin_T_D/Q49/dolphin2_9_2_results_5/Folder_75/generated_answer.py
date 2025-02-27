def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fib = [0, 1]
    i = 1
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[i])
        i += 1
    if n == fib[-2]:
        return True
    return False