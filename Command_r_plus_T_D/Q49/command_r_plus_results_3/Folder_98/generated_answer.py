def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_14th_number = 377
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_14th_number == 0