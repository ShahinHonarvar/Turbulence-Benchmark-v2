def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_110th_num = 31941592653589793238295761
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_110th_num == 0