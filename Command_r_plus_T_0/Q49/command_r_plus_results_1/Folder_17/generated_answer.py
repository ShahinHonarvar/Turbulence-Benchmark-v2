def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_154th_number = 1596959639639095501
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_154th_number == 0