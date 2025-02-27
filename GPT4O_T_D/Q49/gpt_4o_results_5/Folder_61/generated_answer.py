def if_decimal_is_divisible(binary_str):
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    fib_n = 0
    for _ in range(2, 77):
        fib_n = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_n == 0