def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_69 = 117669030460994
    return decimal % fib_69 == 0