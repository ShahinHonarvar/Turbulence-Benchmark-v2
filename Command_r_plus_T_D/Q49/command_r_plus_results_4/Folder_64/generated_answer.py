def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_tenth_num = 55
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_tenth_num == 0