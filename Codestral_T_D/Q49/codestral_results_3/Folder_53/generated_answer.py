def if_decimal_is_divisible(binary_rep):
    decimal = int(binary_rep, 2)
    fib = [0, 1] + [0] * 63
    for i in range(2, 65):
        fib[i] = fib[i - 1] + fib[i - 2]
    return decimal % fib[64] == 0