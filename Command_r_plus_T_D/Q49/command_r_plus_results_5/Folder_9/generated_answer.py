def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_68th_num = 17711
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_68th_num == 0