def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_84th_number = 14930352
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_84th_number == 0