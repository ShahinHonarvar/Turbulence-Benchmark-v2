def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_68th_number = 1836311903
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_68th_number == 0