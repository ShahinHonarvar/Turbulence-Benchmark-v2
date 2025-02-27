def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_39th_number = 63245986
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_39th_number == 0