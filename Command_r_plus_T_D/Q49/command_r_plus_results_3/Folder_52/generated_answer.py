def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_176th_number = 1134903170
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_176th_number == 0