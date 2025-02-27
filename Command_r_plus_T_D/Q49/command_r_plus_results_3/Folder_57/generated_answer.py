def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_80th_number = 23416728348467685
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_80th_number == 0