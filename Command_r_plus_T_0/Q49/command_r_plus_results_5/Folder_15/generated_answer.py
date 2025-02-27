def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_9th_number = 21
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_9th_number == 0