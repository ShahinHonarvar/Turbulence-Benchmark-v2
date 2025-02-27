def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_sixth_number = 8
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_sixth_number == 0