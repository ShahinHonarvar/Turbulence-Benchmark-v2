def if_decimal_is_divisible(binary):
    fib = [0, 1]
    while fib[-1] <= 2 ** len(binary):
        fib.append(fib[-1] + fib[-2])
    return int(binary, 2) % fib[-2] == 0