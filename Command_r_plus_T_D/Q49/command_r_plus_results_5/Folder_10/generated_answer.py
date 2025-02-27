def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_88th_number = 31116927036848
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_88th_number == 0