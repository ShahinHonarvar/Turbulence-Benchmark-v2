def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_108th_number = 12586269025
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_108th_number == 0