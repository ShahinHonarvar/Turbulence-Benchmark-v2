def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_195th_number = 12586269025
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_195th_number == 0