def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1] + [fib_list[-1] + fib_list[-2] for _ in range(2, 99)]
    return int(binary_string, 2) % fib_list[98] == 0