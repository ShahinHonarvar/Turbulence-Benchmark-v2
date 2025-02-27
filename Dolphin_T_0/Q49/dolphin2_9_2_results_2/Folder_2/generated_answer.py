def if_decimal_is_divisible(n):
    fib = [0, 1]
    while len(fib) < 125:
        fib.append(fib[-1] + fib[-2])
    decimal = int(n, 2)
    if decimal % fib[124] == 0:
        return True
    else:
        return False