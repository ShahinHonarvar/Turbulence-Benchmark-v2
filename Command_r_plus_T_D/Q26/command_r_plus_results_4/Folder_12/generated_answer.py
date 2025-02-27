def sum_in_range(numbers_list: list[int]) -> int:
    sum_range = 0
    for num in numbers_list:
        if -91 <= num <= -61:
            sum_range += num
    return sum_range