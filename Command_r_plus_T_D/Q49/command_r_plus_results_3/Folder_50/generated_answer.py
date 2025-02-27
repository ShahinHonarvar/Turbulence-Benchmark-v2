def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_119th_number = 114641114641114640673150763777700284641
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_119th_number == 0