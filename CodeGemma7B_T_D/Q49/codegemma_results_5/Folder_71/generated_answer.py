def if_decimal_is_divisible(binary_string):
    fib_list = [0, 1]
    for i in range(2, len(binary_string)):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    decimal_value = int(binary_string, 2)
    if decimal_value >= fib_list[-1]:
        return False
    elif fib_list.index(decimal_value) != -1:
        return True
    else:
        for i in range(len(fib_list)):
            if decimal_value % fib_list[i] == 0:
                return True
    return False