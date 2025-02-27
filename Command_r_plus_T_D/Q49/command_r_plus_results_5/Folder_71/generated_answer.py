def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_147th_num = 1913470240009327805117924931
    binary_int = int(binary_str, 2)
    if binary_int % fib_147th_num == 0:
        return True
    else:
        return False