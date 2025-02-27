def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_numbers = [num for i, num in enumerate(numbers_list) if num % 2 != 0 and 10 <= i < 79]
    return odd_numbers