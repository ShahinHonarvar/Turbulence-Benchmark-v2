def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_list = [0, 1]
    index = 2
    while fib_list[index - 1] < decimal_num:
        fib_list.append(fib_list[index - 1] + fib_list[index - 2])
        index += 1
    if fib_list[index - 2] > decimal_num:
        return False
    else:
        return decimal_num % fib_list[index - 2] == 0