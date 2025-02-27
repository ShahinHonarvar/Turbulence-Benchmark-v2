def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_45th_number = 1134903170
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fibonacci_45th_number == 0