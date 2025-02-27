def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_38th_num = 2378414852203042802281
    decimal_int = int(binary_str, 2)
    if decimal_int % fib_38th_num == 0:
        return True
    else:
        return False