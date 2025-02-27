def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_13th_number = 233
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_13th_number == 0