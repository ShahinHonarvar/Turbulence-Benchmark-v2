def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_17th_number = 1597
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_17th_number == 0