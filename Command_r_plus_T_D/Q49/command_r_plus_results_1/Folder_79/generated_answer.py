def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_13th_number = 233
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_13th_number == 0