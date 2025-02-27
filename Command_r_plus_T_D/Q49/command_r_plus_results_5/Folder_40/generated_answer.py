def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_4th_number = 3
    decimal_num = int(binary_str, 2)
    if decimal_num % fib_4th_number == 0:
        return True
    else:
        return False