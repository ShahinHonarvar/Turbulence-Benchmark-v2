def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_34th_number = 5702887
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_34th_number == 0