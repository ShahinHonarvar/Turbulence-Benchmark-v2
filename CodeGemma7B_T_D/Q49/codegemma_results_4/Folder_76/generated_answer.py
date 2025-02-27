def if_decimal_is_divisible(binary_num):
    decimal_num = int(binary_num, 2)
    fibonacci_nums = [0, 1]
    for i in range(2, 188):
        fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])
    if decimal_num % fibonacci_nums[-1] == 0:
        return True
    else:
        return False