def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_78th_number = 956722026041
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_78th_number == 0