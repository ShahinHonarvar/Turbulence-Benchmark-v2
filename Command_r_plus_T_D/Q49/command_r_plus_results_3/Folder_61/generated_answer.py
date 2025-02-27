def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_num = 0
    fib_prev = 1
    for _ in range(75):
        fib_num, fib_prev = (fib_num + fib_prev, fib_num)
    target_num = int(binary_str, 2)
    return target_num % fib_num == 0