def if_decimal_is_divisible(binary_num):
    num = int(binary_num, 2)
    fib_num = [0, 1]
    while fib_num[-1] < num:
        fib_num.append(fib_num[-1] + fib_num[-2])
    return num % fib_num[16] == 0