def if_decimal_is_divisible(bi_num):
    fib_num = [0, 1]
    idx = 2
    num = bi_num
    while num >= 1:
        num -= fib_num[idx]
        fib_num.append(fib_num[idx] + fib_num[idx - 1])
        idx += 1
    return num == 0