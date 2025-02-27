def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 199):
        fib.append(fib[-1] + fib[-2])
    fib_198th = fib[198]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_198th == 0