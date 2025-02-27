def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for _ in range(2, 175):
        fib.append(fib[-1] + fib[-2])
    fib_174th = fib[174]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_174th == 0