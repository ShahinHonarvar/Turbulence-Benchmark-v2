def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_19th_number = 4181
    decimal_int = int(binary_str, 2)
    if decimal_int % fib_19th_number == 0:
        return True
    else:
        return False