def if_decimal_is_divisible(binary):
    fib_list = [0, 1]
    fib_number = 1
    for _ in range(15):
        fib_list.append(fib_number)
        fib_number = fib_list[-1] + fib_list[-2]
    int_binary = int(binary, 2)
    return int_binary % fib_list[15] == 0