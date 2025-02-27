def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_84th_number = 102334155
    binary_int = int(binary_str, 2)
    return binary_int % fib_84th_number == 0