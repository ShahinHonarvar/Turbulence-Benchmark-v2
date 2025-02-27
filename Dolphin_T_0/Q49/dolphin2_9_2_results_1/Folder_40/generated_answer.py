def if_decimal_is_divisible(binary):
    n = 0
    while len(bin(n)) < len(binary):
        n += 1
    fib = [0, 1]
    while fib[-1] * fib[-2] < 2 ** (len(binary) - 2):
        fib.append(fib[-1] + fib[-2])
    return int(binary, 2) % fib[3] == 0