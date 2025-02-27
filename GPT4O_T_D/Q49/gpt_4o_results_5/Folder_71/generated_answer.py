def if_decimal_is_divisible(binary_str):
    n_1, n_2 = (0, 1)
    for _ in range(147):
        n_1, n_2 = (n_2, n_1 + n_2)
    decimal_number = int(binary_str, 2)
    return decimal_number % n_1 == 0