def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fib = [0, 1]
    while len(fib) < 77:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[76] == 0