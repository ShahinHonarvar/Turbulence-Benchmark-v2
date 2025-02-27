def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_16th_num = 987
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_16th_num == 0