def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_138th_num = 1389537
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_138th_num == 0