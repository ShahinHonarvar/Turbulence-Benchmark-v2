def sum_in_range(numbers_list: list[int]) -> int:
    sum_in_range = 0
    for number in numbers_list:
        if 10 <= number <= 97:
            sum_in_range += number
    return sum_in_range