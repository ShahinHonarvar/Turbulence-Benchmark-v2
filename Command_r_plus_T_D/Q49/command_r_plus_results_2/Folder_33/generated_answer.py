def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_134th_number = 10610209857723
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_134th_number == 0