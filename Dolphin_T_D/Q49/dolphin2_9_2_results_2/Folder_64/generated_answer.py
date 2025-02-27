def if_decimal_is_divisible(binary_string):
    if_decimal = int(binary_string, 2)
    fib_list = [0, 1]
    for i in range(2, 11):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    if if_decimal % fib_list[10] == 0:
        return True
    else:
        return False