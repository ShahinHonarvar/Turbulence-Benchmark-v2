def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_130th_number = 3654352965218934343
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_130th_number == 0