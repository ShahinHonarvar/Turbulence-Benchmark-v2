def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fib_19 = 4181
    return decimal_number % fib_19 == 0