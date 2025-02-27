def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    i = 2
    target_num = 160 * int(fib_nums[len(fib_nums) - 1]) + int(fib_nums[len(fib_nums) - 2])
    while fib_nums[-1] < target_num:
        fib_nums.append(fib_nums[i] + fib_nums[i - 1])
        i += 1
    return int(binary_str, 2) % fib_nums[-1] == 0