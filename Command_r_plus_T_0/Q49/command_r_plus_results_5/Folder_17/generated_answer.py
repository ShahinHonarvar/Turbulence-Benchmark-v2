def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_154th_number = 15969594819110558545216062122656179689506678496
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_154th_number == 0