def if_decimal_is_divisible(binary_str):
    fib_list = [0, 1]
    for i in range(2, 190):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    dec_num = int(binary_str, 2)
    return dec_num % fib_list[-1] == 0