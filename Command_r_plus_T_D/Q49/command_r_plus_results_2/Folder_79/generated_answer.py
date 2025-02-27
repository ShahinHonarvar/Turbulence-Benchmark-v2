def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_13th = 144
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fibonacci_13th == 0