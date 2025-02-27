def if_decimal_is_divisible(binary_representation):
    dec_num = int(binary_representation, 2)
    fib_list = [0, 1]
    while len(fib_list) <= 186:
        fib_list.append(fib_list[-1] + fib_list[-2])
    if dec_num % fib_list[186] == 0:
        return True
    else:
        return False