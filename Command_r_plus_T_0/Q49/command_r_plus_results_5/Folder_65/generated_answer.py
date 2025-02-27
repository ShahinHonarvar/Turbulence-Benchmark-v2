def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_127th_num = 1913470240009327805117967972713888229
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_127th_num == 0