def sum_in_range(numbers_list: list[int]) -> int:
    lower_bound = -355
    upper_bound = -297
    return sum((i for i in numbers_list if lower_bound <= i <= upper_bound))