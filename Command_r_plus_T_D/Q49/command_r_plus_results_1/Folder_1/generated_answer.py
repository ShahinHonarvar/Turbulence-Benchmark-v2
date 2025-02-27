def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_90th_number = 21892299583455516908654165572574771230816562080
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_90th_number == 0