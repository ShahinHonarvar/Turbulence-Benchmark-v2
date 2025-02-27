def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_56th_num = 196418
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_56th_num == 0