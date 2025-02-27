def if_decimal_is_divisible(binary_str):
    fib_num = 0
    fib_list = [fib_num]
    is_divisible = False
    while not is_divisible:
        fib_num = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_num)
        if len(fib_num) == len(binary_str):
            if int(fib_num) % int(''.join(binary_str)) == 0:
                is_divisible = True
            fib_list.pop(-1)
        elif len(fib_num) > len(binary_str):
            fib_list.pop(-1)
    return is_divisible