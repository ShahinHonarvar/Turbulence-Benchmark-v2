def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_14th_number = 377
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_14th_number == 0