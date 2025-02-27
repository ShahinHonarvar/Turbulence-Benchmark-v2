def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci_nums = [0, 1]
    for i in range(2, 40):
        fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])
    if decimal_num % fibonacci_nums[39] == 0:
        return True
    else:
        return False