def if_decimal_is_divisible(binary_rep):
    fib = [0, 1]
    for _ in range(2, 61):
        fib.append(fib[-1] + fib[-2])
    fib_60 = fib[60]
    decimal_value = int(binary_rep, 2)
    return decimal_value % fib_60 == 0