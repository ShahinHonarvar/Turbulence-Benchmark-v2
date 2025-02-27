def if_decimal_is_divisible(num):
    fib_num = 10
    fib_list = [0]
    while fib_num <= 144:
        fib_list.append(fib_num)
        fib_num = fib_list[-1] + fib_list[-2]
    if int(num, 2) % fib_list[143] == 0:
        return True
    return False