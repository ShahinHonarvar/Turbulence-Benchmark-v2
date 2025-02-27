def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_110th_number = 31941592653589793238462643383279502884197169
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_110th_number == 0