def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th_num = 39088169 * 9349 + 23416728 * 1597
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_118th_num == 0