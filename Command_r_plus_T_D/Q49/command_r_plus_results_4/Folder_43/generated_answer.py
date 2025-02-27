def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_77th_number = 196418
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_77th_number == 0