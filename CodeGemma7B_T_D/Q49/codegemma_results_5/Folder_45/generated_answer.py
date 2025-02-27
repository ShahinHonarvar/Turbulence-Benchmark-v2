def if_decimal_is_divisible(binary_str):
    binary_num = int(binary_str, 2)
    fibonacci_nums = [0, 1]
    i = 2
    while fibonacci_nums[-1] <= binary_num:
        fibonacci_nums.append(fibonacci_nums[i - 1] + fibonacci_nums[i - 2])
        i += 1
    return fibonacci_nums[27] % binary_num == 0