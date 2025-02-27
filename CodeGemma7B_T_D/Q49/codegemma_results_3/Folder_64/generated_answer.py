def decimal_is_divisible(binary_string):
    fib_nums = [0, 1]
    next_fib = 1
    while next_fib <= 10 * int(binary_string[-1]):
        fib_nums.append(next_fib)
        next_fib = fib_nums[-1] + fib_nums[-2]
    return int(binary_string, 2) in fib_nums