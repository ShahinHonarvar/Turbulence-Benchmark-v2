def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 134:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[133] == 0