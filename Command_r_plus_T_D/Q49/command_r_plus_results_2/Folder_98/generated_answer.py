def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_14th = 377
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_14th == 0