def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fib_nums = [0, 1]
    while len(fib_nums) < 74:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    fib_74 = fib_nums[73]
    return decimal_num % fib_74 == 0