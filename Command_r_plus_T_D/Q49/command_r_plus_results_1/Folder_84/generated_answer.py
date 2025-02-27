def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_196th_number = 2080270050190671
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_196th_number == 0