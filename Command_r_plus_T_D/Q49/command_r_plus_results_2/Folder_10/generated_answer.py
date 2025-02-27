def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_88th_number = 354224848179261915075
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_88th_number == 0