def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_numbers = [num for i, num in enumerate(numbers_list) if i >= 68 and i < 99 and (num % 2 != 0)]
    return odd_numbers