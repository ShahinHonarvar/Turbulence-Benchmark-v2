def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_179th_num = 12200160415121876738
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_179th_num == 0