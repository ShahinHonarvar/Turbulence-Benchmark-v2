def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fib_num = [0, 1]
    while len(fib_num) < 134:
        fib_num.append(fib_num[-2] + fib_num[-1])
    if decimal_num % fib_num[133] == 0:
        return True
    else:
        return False