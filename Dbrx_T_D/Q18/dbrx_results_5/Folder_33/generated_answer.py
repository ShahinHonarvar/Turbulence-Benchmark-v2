def sum_ints_div_by_either_nums(numbers):
    start_index = 281
    end_index = 694
    if end_index >= len(numbers):
        return 0
    sum_of_divisible_ints = 0
    divisible_nums = set([-722, -731])
    for i in range(start_index, end_index + 1):
        if numbers[i] in divisible_nums or numbers[i] % -722 == 0 or numbers[i] % -731 == 0:
            sum_of_divisible_ints += numbers[i]
    return sum_of_divisible_ints