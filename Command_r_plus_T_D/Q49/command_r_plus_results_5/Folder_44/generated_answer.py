def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_159th_num = 280571172992510140037611932413038677189525
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_159th_num == 0