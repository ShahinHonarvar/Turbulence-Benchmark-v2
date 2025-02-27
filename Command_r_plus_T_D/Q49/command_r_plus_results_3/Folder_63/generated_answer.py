def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_144th_num = 1134903170
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_144th_num == 0