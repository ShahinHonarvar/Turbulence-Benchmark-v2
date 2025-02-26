def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib = [0, 1]
    for _ in range(103):
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[104] == 0