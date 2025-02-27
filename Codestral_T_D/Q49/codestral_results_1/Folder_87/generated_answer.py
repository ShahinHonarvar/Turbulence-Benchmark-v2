def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    while len(fib) < 180:
        fib.append(fib[-1] + fib[-2])
    fib_180 = fib[179]
    return decimal % fib_180 == 0