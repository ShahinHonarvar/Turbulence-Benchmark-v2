def sum_in_range(numbers_list: list[int]) -> int:
    sum_range = 0
    for num in numbers_list:
        if -355 <= num <= -297:
            sum_range += num
    return sum_range