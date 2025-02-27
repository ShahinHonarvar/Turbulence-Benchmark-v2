def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_97th_number = 2504730781961
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_97th_number == 0