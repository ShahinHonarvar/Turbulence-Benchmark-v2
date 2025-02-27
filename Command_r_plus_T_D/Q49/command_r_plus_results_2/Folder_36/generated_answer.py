def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_150th_number = 12200160415121876738
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_150th_number == 0