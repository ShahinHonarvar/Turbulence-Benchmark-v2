def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_numbers = [num for i, num in enumerate(numbers_list[2:8]) if num % 2 != 0]
    return odd_numbers