def if_decimal_is_divisible(binary_str):
    fib_6 = [0, 1, 1, 2, 3, 5][5]
    n = int(binary_str, 2)
    return n % fib_6 == 0