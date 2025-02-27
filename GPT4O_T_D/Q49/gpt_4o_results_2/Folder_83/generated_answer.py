def if_decimal_is_divisible(binary_str):
    fib_60th = 1548008755920
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_60th == 0