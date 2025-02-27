def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_10th_number = 55
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_10th_number == 0