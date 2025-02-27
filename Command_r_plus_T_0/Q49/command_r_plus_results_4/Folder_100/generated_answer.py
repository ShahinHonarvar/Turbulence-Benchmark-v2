def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_190th_number = 222668507353049617089
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_190th_number == 0