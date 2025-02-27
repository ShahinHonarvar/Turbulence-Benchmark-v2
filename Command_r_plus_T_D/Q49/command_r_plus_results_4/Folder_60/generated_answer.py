def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_108th_number = 832040
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_108th_number == 0