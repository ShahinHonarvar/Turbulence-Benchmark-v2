def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_150th = 225851433717
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_150th == 0