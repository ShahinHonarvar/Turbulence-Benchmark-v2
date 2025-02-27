def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_35th_num = 9227465
    decimal_num = int(binary_str, 2)
    if decimal_num % fib_35th_num == 0:
        return True
    else:
        return False