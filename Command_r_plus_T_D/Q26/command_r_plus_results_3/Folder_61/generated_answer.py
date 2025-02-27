def sum_in_range(numbers_list: list[int]) -> int:
    sum_in_range = 0
    for num in numbers_list:
        if 8 <= num <= 9:
            sum_in_range += num
    return sum_in_range