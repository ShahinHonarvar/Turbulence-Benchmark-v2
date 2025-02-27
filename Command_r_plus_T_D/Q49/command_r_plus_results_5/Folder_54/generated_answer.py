def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_34th_number = 5702887
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_34th_number == 0