def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_168 = 16640803821257342614273
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_168 == 0