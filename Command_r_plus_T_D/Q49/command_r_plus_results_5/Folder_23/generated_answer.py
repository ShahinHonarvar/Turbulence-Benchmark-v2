def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_48th_num = 1134903170
    decimal_val = int(binary_str, 2)
    return decimal_val % fib_48th_num == 0