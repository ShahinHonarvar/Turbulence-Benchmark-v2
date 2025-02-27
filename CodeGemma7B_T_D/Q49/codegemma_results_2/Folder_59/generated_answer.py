def if_decimal_is_divisible(binary_str):
    fib_nums = [0, 1]
    fib_num = 2
    while fib_num < 75:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        fib_num += 1
    decimal_int = int(binary_str, 2)
    return decimal_int % fib_nums[74] == 0