def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_15th_number = 610
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_15th_number == 0