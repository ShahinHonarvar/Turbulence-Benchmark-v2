def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_74th_number = 130700730061781188631582330661768208400207891983
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_74th_number == 0