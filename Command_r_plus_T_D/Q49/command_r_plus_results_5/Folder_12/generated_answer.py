def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_66th = 121393
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_66th == 0