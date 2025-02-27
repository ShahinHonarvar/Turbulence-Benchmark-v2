def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_164th_number = 1364234299291444641725763940264041257067
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_164th_number == 0