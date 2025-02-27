def if_decimal_is_divisible(binary_str):
    fib_1, fib_2 = (0, 1)
    for _ in range(185):
        fib_1, fib_2 = (fib_2, fib_1 + fib_2)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_2 == 0