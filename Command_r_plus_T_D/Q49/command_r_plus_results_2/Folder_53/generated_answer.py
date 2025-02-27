def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_64th_number = 184562302034524043121
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_64th_number == 0