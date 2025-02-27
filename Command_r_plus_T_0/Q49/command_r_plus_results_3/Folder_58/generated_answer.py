def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_105th_number = 139583862445
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_105th_number == 0