def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci_nums = [0, 1]
    while fibonacci_nums[-1] < decimal_integer:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    if len(fibonacci_nums) < 159:
        return False
    return decimal_integer % fibonacci_nums[158] == 0