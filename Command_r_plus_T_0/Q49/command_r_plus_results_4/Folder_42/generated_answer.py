def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_146th = 24157817
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_146th == 0