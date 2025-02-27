def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_166th_number = 987
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_166th_number == 0