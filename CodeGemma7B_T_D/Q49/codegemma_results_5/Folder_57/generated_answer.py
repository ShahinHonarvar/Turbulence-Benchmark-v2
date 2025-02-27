def if_decimal_is_divisible(bin_num):
    fib_num = 0
    fib_nums = [0]
    fib_index = 0
    fib_count = 0
    non_fib_index = 0
    while fib_index < len(bin_num) * 2:
        fib_index += 1
        fib_num = fib_nums[-1] + fib_nums[-2]
        fib_nums.append(fib_num)
        if fib_num >= 80:
            fib_count += 1
            if fib_count == len(bin_num) + 1:
                non_fib_index = fib_index
                break
    fib_count = 0
    bin_num_dec = 0
    while bin_num_dec < len(bin_num) * 8 + 1:
        bin_num_dec += 1
        if non_fib_index != bin_num_dec:
            if bin_num[-1] == '1':
                bin_num_dec += 1
                bin_num = bin_num[:-1]
    if bin_num_dec == 0:
        return True
    elif non_fib_index == fib_index - 1:
        return True
    else:
        return False