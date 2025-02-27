def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_188 = 1503474000312591800015419322261118683169471844891433693811819
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_188 == 0