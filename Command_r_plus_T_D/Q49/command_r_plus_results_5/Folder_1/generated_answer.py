def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_90th_number = 218922995834555169089
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_90th_number == 0