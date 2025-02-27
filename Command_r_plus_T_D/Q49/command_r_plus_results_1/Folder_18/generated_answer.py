def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_199th = 199426993915979425313328870933846029818963131314282289598512169030942742327122456926189690164
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_199th == 0