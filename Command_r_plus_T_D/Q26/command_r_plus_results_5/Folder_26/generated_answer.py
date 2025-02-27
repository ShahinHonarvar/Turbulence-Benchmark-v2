def sum_in_range(numbers: list[int]) -> int:
    lower_bound = -355
    upper_bound = -297
    return sum((i for i in numbers if lower_bound <= i <= upper_bound))