def if_decimal_is_divisible(binary_str):
    fib_1, fib_2 = (0, 1)
    for _ in range(125):
        fib_1, fib_2 = (fib_2, fib_1 + fib_2)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_1 == 0