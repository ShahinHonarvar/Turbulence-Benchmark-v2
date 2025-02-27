def sum_in_range(numbers_list: list[int]) -> int:
    lower_bound = -355
    upper_bound = -297
    return sum((num for num in numbers_list if lower_bound <= num <= upper_bound))