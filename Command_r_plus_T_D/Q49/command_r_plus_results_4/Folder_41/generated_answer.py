def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_67th_num = 19070076485849042169865124651289
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_67th_num == 0