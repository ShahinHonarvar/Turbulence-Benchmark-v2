def if_decimal_is_divisible(binary_string):
    fib_nums = [0, 1]
    while len(fib_nums) < 191:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    decimal_num = int(binary_string, 2)
    return decimal_num % fib_nums[190] == 0