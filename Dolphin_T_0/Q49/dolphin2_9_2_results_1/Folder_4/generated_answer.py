def if_decimal_is_divisible(binary_representation):
    decimal_value = 0
    for digit in binary_representation:
        decimal_value = decimal_value * 2 + int(digit)
    fibonacci_nums = [0, 1]
    for _ in range(2, 118):
        fibonacci_nums.append(fibonacci_nums[-1] + fibonacci_nums[-2])
    return decimal_value % fibonacci_nums[117] == 0