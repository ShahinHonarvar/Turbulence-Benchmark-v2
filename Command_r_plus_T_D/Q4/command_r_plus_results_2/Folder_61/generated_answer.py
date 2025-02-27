def all_pos_ints_exclusive(numbers_list: list[int]) -> list[int]:
    positive_numbers = [num for num in numbers_list[0:8] if num > 0]
    return positive_numbers