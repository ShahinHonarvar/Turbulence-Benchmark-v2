def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_34th_number = 5702887
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_34th_number == 0