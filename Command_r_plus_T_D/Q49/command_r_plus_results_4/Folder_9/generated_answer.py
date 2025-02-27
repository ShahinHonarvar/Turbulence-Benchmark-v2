def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_68th_number = 956722026041
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_68th_number == 0