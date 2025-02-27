def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_166th_num = 13059561328288054473081277268237652
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_166th_num == 0