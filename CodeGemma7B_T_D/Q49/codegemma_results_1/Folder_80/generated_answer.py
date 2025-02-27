def if_decimal_is_divisible(binary_representation):
    fib_nums = [0, 1]
    current_num = 2
    while fib_nums[-1] + fib_nums[-2] <= int(binary_representation, 2):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        current_num += 1
    return fib_nums[-1] % int(binary_representation, 2) == 0