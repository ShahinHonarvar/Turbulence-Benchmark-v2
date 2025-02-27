def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th_number = 39088169
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_118th_number == 0