def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_num = 0
    fib_next = 1
    for _ in range(77):
        fib_num, fib_next = (fib_next, fib_num + fib_next)
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_num == 0