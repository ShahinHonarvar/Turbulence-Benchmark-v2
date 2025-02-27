def if_decimal_is_divisible(binary_string):
    binary_list = list(binary_string)
    binary_list.reverse()
    binary_num = 0
    for i in range(len(binary_list)):
        binary_num += int(binary_list[i]) * 2 ** i
    fib_list = [0, 1]
    for i in range(2, 169):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    fib_num = fib_list[168]
    if binary_num % fib_num == 0:
        return True
    else:
        return False