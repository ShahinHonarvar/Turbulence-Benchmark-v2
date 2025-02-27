def sum_in_range(numbers_list: list[int]) -> int:
    sum_in_range = 0
    for num in numbers_list:
        if 1 <= num <= 8:
            sum_in_range += num
    return sum_in_range