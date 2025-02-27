def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_146th_number = 24157817
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_146th_number == 0