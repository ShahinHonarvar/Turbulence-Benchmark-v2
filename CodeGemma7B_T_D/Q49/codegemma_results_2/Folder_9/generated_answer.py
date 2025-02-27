def if_decimal_is_divisible(binary_str):
    decimal_int = int(binary_str, 2)
    fibonacci_nums = [0, 1]
    while len(fibonacci_nums) <= 68:
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_int % fibonacci_nums[68] == 0