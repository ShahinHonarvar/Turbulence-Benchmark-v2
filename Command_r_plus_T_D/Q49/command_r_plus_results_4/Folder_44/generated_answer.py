def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_159th_number = 10610209857723
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_159th_number == 0