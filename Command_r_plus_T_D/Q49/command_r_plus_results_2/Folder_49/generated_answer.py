def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_95th_number = 121393
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_95th_number == 0