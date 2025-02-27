def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_120th_number = 12200160415121876738
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_120th_number == 0