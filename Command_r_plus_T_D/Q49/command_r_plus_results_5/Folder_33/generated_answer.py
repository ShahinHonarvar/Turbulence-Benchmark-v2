def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_134th_num = 10610209857723
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_134th_num == 0