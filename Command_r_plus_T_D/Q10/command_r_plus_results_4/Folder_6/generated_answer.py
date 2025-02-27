def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_ints_range = [num for i, num in enumerate(numbers_list[86:99]) if num % 2 != 0]
    return odd_ints_range