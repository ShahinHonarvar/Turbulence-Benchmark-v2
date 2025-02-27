def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_87th_number = 51090942171709440000
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_87th_number == 0