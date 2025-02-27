def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_numbers = [num for num in numbers_list[62:96] if num % 2 != 0]
    return odd_numbers