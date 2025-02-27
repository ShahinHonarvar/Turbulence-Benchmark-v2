def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_24th_number = 46368
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_24th_number == 0