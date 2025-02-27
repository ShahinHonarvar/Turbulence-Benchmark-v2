def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_164th_num = 19541627284643493102365188455564279379012227021458554671
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_164th_num == 0