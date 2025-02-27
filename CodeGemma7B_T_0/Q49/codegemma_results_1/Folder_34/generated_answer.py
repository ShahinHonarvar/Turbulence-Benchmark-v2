def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    fib_index = 2
    while fib_nums[-1] < 24 * int(binary_str, 2):
        fib_nums.append(fib_nums[fib_index - 1] + fib_nums[fib_index - 2])
        fib_index += 1
    return fib_nums[-1] % 24 == 0