def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_134th_number = 10610209857723
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_134th_number == 0