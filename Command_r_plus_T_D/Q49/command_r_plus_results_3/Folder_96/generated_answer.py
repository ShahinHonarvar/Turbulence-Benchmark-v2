def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_47th_number = 2971215073
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_47th_number == 0