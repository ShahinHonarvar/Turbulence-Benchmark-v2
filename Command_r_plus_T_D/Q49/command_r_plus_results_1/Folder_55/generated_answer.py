def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_39th_number = 63245986
    decimal_integer = int(binary_str, 2)
    return decimal_integer % fib_39th_number == 0