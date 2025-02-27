def if_decimal_is_divisible(binary):
    fib_list = [0, 1]
    while len(fib_list) < 190:
        fib_list.append(fib_list[-1] + fib_list[-2])
    decimal = int(binary, 2)
    return decimal % fib_list[189] == 0