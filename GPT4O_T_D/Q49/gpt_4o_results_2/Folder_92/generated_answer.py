def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    seventh_fib_number = 8
    return decimal_value % seventh_fib_number == 0