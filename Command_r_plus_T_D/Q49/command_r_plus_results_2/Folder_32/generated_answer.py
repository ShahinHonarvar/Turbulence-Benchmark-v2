def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_178th_number = 1548008755920
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_178th_number == 0