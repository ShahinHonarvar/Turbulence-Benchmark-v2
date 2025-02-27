def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_150th_num = 12586269025
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_150th_num == 0