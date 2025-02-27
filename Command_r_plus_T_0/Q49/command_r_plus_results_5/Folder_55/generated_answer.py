def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_39th_number = 63245986
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fibonacci_39th_number == 0