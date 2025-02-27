def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_170th_number = 19089730604690271531562474014329370944
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_170th_number == 0