def if_decimal_is_divisible(binary):
    fib = [0]
    n = 2
    for _ in range(40):
        fib.append(fib[-1] + fib[-2])
    decimal = int(binary, 2)
    return decimal % fib[40] == 0