def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fib_list = [0, 1]
    for i in range(2, 175):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    if decimal_num % fib_list[174] == 0:
        return True
    else:
        return False