def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_56th_number = 196418
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_56th_number == 0