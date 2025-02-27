def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fib_n_1, fib_n_2 = (0, 1)
    for _ in range(114):
        fib_n_1, fib_n_2 = (fib_n_2, fib_n_1 + fib_n_2)
    return decimal_number % fib_n_2 == 0