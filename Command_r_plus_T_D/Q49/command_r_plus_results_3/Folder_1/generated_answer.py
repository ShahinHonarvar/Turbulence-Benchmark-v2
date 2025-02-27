def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_90th_num = 218922995834555169086541632838011881869260971310203151480358416029284893403868808843464064
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_90th_num == 0