def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_176th_number = 12586269025
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_176th_number == 0