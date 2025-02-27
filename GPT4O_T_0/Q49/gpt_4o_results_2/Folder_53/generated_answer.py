def if_decimal_is_divisible(binary_str):
    fib_64 = 10610209857723
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_64 == 0