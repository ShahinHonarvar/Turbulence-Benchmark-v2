def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_47th_number = 2971215073
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_47th_number == 0