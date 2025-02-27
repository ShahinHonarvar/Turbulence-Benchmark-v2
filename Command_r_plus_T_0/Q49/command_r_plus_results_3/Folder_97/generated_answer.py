def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_114th_num = 130554762408224617
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_114th_num == 0