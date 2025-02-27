def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_97th_num = 2504730781961
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_97th_num == 0