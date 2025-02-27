def if_decimal_is_divisible(binary_str):
    fib_n1, fib_n2 = (0, 1)
    for _ in range(185):
        fib_n1, fib_n2 = (fib_n2, fib_n1 + fib_n2)
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_n2 == 0