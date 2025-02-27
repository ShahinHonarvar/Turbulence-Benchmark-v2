def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_137th_num = 195416237398990716402719
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_137th_num == 0