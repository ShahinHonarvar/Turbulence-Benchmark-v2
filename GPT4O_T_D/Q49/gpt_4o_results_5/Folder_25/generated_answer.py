def if_decimal_is_divisible(binary_str):
    target_fib_number = 4181
    decimal_number = int(binary_str, 2)
    return decimal_number % target_fib_number == 0