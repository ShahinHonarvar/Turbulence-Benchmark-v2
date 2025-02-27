def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_56th_number = 178657
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_56th_number == 0