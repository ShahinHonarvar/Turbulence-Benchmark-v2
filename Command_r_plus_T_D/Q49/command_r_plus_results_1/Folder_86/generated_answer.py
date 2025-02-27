def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_135th = 32951280099
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_135th == 0