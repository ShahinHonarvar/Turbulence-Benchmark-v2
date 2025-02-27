def if_decimal_is_divisible(binary_num):
    curr_num = 0
    fib_num = 46
    i = len(binary_num) - 1
    while i >= 0:
        curr_num += 2 ** i * int(binary_num[i])
        if curr_num >= fib_num and curr_num % fib_num == 0:
            return True
        if curr_num > fib_num:
            fib_num += fib_num - 46
        i -= 1
    return False