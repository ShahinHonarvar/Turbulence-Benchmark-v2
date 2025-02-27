def if_decimal_is_divisible(bin_str):
    decimal_num = int(bin_str, 2)
    fibonacci_nums = [0, 1]
    while fibonacci_nums[-1] < decimal_num:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    if len(fibonacci_nums) >= 180 and decimal_num % fibonacci_nums[179] == 0:
        return True
    else:
        return False