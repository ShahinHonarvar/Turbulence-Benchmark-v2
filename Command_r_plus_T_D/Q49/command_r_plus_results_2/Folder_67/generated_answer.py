def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_107th_number = 19541
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_107th_number == 0