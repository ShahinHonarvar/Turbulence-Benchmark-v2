def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_29th_number = 514229
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_29th_number == 0