def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_105th_number = 20365
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_105th_number == 0