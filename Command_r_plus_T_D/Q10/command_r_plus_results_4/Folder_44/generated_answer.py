def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_ints_range = [num for i, num in enumerate(numbers_list) if (i >= 81 and i < 86) and num % 2 != 0]
    return odd_ints_range