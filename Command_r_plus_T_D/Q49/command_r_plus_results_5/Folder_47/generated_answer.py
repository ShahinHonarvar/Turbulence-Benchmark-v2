def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_94th_num = 102334155
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_94th_num == 0