def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_196th = 222117742518820522201
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_196th == 0