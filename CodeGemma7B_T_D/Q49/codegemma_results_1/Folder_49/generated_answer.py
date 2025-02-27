def if_decimal_is_divisible(binary):
    fib_list = [0]
    fib_n = 0
    for i in range(1, 95):
        fib_n = fib_list[i - 1] + fib_list[i - 2]
        fib_list.append(fib_n)
    fib_num = int(binary, 2)
    if fib_num % fib_list[94] == 0:
        return True
    else:
        return False