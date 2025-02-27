def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_47th_num = 2971215073
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_47th_num == 0