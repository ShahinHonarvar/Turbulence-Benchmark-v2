def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    while len(fib) < 127:
        fib.append(fib[-1] + fib[-2])
    return int(binary_str, 2) % fib[126] == 0