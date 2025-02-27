def if_decimal_is_divisible(binary_str):
    fib_number = 317811
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_number == 0