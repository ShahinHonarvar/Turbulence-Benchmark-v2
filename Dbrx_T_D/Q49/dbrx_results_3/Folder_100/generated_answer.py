def if_decimal_is_divisible(binary_rep):
    decimal_num = int(binary_rep, 2)
    fibonacci_nums = [0, 1]
    while fibonacci_nums[-1] < decimal_num:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_num % fibonacci_nums[190] == 0