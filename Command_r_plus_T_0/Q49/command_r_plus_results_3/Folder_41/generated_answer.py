def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_67th_number = 1907556569
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_67th_number == 0