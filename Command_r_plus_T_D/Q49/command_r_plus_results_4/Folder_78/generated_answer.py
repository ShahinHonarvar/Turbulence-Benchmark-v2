def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_115th_num = 1346269
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_115th_num == 0