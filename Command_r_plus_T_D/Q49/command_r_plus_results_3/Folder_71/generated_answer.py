def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_147th_num = 195416725447999126500
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_147th_num == 0