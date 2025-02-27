def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_190th_number = 222668550253835455614773135230050550
    binary_as_int = int(binary_str, 2)
    return binary_as_int % fib_190th_number == 0