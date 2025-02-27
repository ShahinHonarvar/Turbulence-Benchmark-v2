def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_54th_number = 182664660901
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_54th_number == 0