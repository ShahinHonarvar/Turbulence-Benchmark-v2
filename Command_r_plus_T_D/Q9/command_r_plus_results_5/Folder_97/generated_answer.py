def all_odd_ints_inclusive(numbers_list: list[int]) -> list[int]:
    odd_numbers = [num for num in numbers_list[40:81] if num % 2 != 0]
    return odd_numbers