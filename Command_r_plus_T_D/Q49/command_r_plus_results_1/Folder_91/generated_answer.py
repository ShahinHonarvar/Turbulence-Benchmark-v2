def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_sixth_number = 8
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_sixth_number == 0