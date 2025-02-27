def if_decimal_is_divisible(binary_num):
    n = int(binary_num, 2)
    fibonacci_nums = [0, 1]
    for i in range(2, 196):
        fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])
    return n % fibonacci_nums[195] == 0