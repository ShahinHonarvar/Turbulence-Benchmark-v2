def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_190th_number = 222668549595571
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_190th_number == 0