def if_decimal_is_divisible(num_str):
    fib_nums = [0, 1]
    while fib_nums[-1] < num_str:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return int(num_str, 2) in fib_nums[189:]