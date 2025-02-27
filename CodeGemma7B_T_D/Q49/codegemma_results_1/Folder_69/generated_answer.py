def if_decimal_is_divisible(bin_representation):
    fib_num_list = [0, 1]
    current_fib_num = 2
    while current_fib_num <= 170:
        fib_num_list.append(current_fib_num)
        current_fib_num = fib_num_list[-1] + fib_num_list[-2]
    decimal_representation = int(bin_representation, 2)
    for num in fib_num_list:
        if decimal_representation % num == 0:
            return True
    return False