def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_20th = 6765
    decimal = int(binary_str, 2)
    return decimal % fib_20th == 0