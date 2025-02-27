def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_74th_number = 14472334024676221
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_74th_number == 0