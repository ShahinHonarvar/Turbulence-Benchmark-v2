def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_88th_number = 354224848179261915075
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_88th_number == 0