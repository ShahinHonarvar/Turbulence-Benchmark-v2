def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_110th_number = 31941592653589793238462643383279502884197169
    decimal_from_binary = int(binary_str, 2)
    return decimal_from_binary % fib_110th_number == 0