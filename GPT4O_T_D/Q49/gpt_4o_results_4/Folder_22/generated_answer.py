def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) < 21:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_number % fibonacci_nums[20] == 0