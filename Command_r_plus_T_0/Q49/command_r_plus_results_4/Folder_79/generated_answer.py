def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_13th_number = 233
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_13th_number == 0