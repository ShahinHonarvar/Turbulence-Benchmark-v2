def if_decimal_is_divisible(binary_str):
    n = int(binary_str, 2)
    fib_20 = (5 + 5 ** 0.5 / 2) ** 20 / (5 ** 0.5 / 2 + 1)
    return n % fib_20 == 0