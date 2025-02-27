def if_decimal_is_divisible(bin_str):
    decimal = int(bin_str, 2)
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1
    for _ in range(188):
        fib_n = fib_n_minus_2 + fib_n_minus_1
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
    return decimal % fib_n == 0