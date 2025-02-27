def if_decimal_is_divisible(binary_str: str) -> bool:
    fibonacci_76th_number = 190097296875
    decimal_int = int(binary_str, 2)
    return decimal_int % fibonacci_76th_number == 0