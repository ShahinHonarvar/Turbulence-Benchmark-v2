def if_decimal_is_divisible(binary):
    num = int(binary, 2)
    fib = [0]
    a, b = (0, 1)
    while len(fib) < 16:
        a, b = (b, a + b)
        fib.append(b)
    return num % fib[15] == 0