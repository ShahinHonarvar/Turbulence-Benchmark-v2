def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_97th_number = 21499909451206374
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_97th_number == 0