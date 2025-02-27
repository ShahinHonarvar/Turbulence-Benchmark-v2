def sum_in_range(numbers_list: list[int]) -> int:
    return sum((num for num in numbers_list if 2 <= num <= 3))