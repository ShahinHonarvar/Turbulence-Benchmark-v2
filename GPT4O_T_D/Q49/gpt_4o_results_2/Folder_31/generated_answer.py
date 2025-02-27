def if_decimal_is_divisible(binary_str):
    fib_69 = 117669030460994
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_69 == 0