def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_46th_number = 1836311903
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fibonacci_46th_number == 0