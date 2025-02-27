def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_35th = 9227465
    decimal_num = int(binary_str, 2)
    return decimal_num % fibonacci_35th == 0