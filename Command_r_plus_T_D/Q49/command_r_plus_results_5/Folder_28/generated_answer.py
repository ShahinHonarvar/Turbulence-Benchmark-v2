def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_104th_number = 12200160415121876738
    binary_str_as_int = int(binary_str, 2)
    if binary_str_as_int % fib_104th_number == 0:
        return True
    else:
        return False