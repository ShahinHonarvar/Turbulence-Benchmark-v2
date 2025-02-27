def if_decimal_is_divisible(binary_str: str) -> bool:
    fib_80th_num = 0
    idx = 1
    while idx <= 80:
        if idx > 2:
            fib_80th_num = fib_80th_num + fib_80th_num_prev
            fib_80th_num_prev = fib_80th_num - fib_80th_num_prev
        else:
            fib_80th_num = idx
        idx += 1
    decimal_num = int(binary_str, 2)
    return decimal_num % fib_80th_num == 0