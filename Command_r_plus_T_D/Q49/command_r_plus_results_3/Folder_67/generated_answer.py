def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_107th_num = 19075565093904508657362701424546378582421932775789776409875024528402410561294170677971761
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_107th_num == 0