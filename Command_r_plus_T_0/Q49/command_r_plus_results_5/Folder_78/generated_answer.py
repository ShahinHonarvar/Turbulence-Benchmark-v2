def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_115th_number = 19740274219868223167
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_115th_number == 0