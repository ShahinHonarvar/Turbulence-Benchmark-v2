def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_97th_number = 214999091986280979437
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_97th_number == 0