def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_190th_num = 218922995834555169086541656538248314309
    binary_decimal = int(binary_str, 2)
    return binary_decimal % fib_190th_num == 0