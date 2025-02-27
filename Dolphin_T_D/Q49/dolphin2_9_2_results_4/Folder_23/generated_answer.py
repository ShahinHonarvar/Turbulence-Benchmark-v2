def if_decimal_is_divisible(bin_rep):
    dec_num = int(bin_rep, 2)
    fib_nums = [0, 1]
    while len(fib_nums) < 48:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return dec_num % fib_nums[47] == 0