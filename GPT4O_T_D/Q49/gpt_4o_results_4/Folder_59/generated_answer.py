def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    for _ in range(72):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    fib_74th = fib_nums[73]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_74th == 0