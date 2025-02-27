def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_179th_number = 12586269025
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_179th_number == 0