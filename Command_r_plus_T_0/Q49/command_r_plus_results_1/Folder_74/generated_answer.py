def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_166 = 12586269025
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_166 == 0