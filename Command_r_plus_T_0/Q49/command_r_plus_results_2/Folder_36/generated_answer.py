def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_150th = 2236639177865511427619
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_150th == 0