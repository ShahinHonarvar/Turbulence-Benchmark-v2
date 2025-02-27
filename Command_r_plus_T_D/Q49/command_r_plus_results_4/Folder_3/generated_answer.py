def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_35th_number = 9227465
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci_35th_number == 0