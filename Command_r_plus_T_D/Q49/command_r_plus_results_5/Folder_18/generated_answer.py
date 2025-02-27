def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_199th_num = 199799806132483250471022475371830580382243167718182044358886811449
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_199th_num == 0