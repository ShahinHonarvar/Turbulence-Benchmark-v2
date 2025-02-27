def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_69th_number = 102334155
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_69th_number == 0