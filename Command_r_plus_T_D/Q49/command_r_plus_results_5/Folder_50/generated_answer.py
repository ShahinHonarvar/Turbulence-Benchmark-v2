def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_119th_num = 1913470240009327805175395783406644508609863289471016403633783790
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_119th_num == 0