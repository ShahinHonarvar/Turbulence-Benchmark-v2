def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_189th = 188 * 189 + 187
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_189th == 0