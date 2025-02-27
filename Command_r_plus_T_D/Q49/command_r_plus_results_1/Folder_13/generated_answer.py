def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_174th_num = 136076694492351404764361802315388168420416
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_174th_num == 0