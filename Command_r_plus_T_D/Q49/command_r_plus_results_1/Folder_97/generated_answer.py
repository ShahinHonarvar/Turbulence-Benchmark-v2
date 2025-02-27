def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_114th_num = 320627465350661
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_114th_num == 0