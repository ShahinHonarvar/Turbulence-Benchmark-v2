def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_88th_number = 31116927036848
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_88th_number == 0