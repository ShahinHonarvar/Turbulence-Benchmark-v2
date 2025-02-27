def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_127th_number = 1954168376706139571666163249696612000
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_127th_number == 0