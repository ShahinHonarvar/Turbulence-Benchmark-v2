def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_175th_num = 1134903170
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_175th_num == 0