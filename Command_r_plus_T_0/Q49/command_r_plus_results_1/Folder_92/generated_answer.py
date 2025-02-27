def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_seventh_number = 13
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_seventh_number == 0