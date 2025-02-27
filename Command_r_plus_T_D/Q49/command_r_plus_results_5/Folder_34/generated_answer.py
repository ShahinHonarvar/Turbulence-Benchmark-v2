def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_24th_num = 46368
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_24th_num == 0