def if_decimal_is_divisible(binary_str):
    fib_104 = 542322581629351702274556143987540822205474640749699305593729
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_104 == 0