def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_78th_number = 956722026041
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_78th_number == 0