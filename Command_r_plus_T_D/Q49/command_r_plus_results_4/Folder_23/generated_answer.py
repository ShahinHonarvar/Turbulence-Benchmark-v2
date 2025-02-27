def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_48 = 1134903170
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_48 == 0