def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_40th_number = 102334155
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_40th_number == 0