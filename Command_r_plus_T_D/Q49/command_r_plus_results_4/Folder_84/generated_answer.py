def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_196th_num = 2221177392256713082317331978176915032001
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_196th_num == 0