def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_185th_number = 12200160415121879276444572534438239811812345725921229633473128788952912132755606253
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_185th_number == 0