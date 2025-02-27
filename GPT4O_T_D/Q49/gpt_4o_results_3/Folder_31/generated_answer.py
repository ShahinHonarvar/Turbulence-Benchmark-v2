def if_decimal_is_divisible(binary_str):
    fibonacci_nums = [0, 1]
    for _ in range(2, 70):
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    decimal_value = int(binary_str, 2)
    return decimal_value % fibonacci_nums[69] == 0