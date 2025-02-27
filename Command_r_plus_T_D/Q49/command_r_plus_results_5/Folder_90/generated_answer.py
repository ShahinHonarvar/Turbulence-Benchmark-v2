def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_177th_num = 15142746488213525
    binary_int = int(binary_str, 2)
    return binary_int % fib_177th_num == 0