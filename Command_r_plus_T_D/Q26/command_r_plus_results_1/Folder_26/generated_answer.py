def sum_in_range(numbers: list[int]) -> int:
    lower_bound = -355
    upper_bound = -297
    return sum((num for num in numbers if lower_bound <= num <= upper_bound))