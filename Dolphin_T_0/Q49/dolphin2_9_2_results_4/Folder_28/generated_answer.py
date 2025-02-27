def if_decimal_is_divisible(binary_rep):
    dec_num = int(binary_rep, 2)
    fib_nums = [0, 1]
    a = 0
    b = 1
    while len(fib_nums) < 104:
        fib_nums.append(a)
        a, b = (b, a + b)
    return dec_num % fib_nums[103] == 0