def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_num = 0
    fib_prev = 0
    for _ in range(77):
        fib_num, fib_prev = (fib_num + fib_prev, fib_num)
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_num == 0