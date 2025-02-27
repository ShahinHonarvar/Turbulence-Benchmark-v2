def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_178th_num = 1954959249
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_178th_num == 0