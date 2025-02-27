def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_28 = 317811
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_28 == 0