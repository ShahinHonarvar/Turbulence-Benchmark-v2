def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_118th_number = 1988990559204698501321169581105578692268073250682185761795
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_118th_number == 0