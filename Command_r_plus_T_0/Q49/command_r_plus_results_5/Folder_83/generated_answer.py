def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_60th_number = 1548008755920
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_60th_number == 0