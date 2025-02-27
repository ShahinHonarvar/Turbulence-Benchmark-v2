def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_130th_number = 354224848179261915075
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_130th_number == 0