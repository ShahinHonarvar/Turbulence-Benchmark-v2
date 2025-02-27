def if_decimal_is_divisible(binary_string):
    decimal_num = int(binary_string, 2)
    fibonacci_nums = [0, 1]
    for _ in range(168):
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    if decimal_num == 0:
        return fibonacci_nums[170] % decimal_num == 0
    else:
        return fibonacci_nums[170] % decimal_num == 0