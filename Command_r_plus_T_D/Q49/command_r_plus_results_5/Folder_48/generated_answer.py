def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_198th_num = 946912847427851840642418075810700433201209763049456630894097681842474224795573101
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_198th_num == 0