def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_107th_num = 19541
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_107th_num == 0