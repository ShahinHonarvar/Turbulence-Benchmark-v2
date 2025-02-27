def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_nums = [0, 1]
    while fibonacci_nums[-1] < decimal_integer:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    target_fibonacci_num = fibonacci_nums[28]
    return decimal_integer % target_fibonacci_num == 0