def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_114th_number = 12586269025
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_114th_number == 0