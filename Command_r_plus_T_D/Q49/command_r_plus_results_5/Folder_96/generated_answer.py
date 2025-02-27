def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_47th_number = 2971215073
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fibonacci_47th_number == 0