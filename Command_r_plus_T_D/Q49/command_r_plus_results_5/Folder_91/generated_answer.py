def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_6th_num = 8
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_6th_num == 0