def if_decimal_is_divisible(s):
    fib_dict = {0: 0, 1: 1}
    for i in range(2, 203):
        fib_dict[i] = fib_dict[i - 2] + fib_dict[i - 1]
    return int(s, 2) % fib_dict[188] == 0