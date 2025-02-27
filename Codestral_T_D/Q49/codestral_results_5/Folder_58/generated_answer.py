def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_num = 0
    prev_num = 0
    curr_num = 1
    for _ in range(105):
        fib_num = prev_num + curr_num
        prev_num = curr_num
        curr_num = fib_num
    if decimal_num % fib_num == 0:
        return True
    else:
        return False