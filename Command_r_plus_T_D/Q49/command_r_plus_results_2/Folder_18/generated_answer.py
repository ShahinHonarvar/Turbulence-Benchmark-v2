def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_199th_number = 12586269025
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_199th_number == 0