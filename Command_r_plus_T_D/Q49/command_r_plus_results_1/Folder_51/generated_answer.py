def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_17th_number = 1597
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_17th_number == 0