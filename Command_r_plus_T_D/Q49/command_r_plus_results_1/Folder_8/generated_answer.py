def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_54th_number = 182664660000000000000000000000000000000000000000000000
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_54th_number == 0