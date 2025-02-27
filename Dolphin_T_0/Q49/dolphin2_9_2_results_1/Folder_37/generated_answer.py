def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fib_nums = [0, 1]
    for i in range(2, 46):
        fib_nums.append(fib_nums[i - 1] + fib_nums[i - 2])
    return n % fib_nums[45] == 0