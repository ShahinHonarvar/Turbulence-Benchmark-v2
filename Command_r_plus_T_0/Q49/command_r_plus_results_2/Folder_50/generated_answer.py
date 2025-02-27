def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_119th_number = 1198132695692156213059
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_119th_number == 0