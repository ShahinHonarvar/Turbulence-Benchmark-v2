def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_108th_number = 832040
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_108th_number == 0