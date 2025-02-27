def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_integers = [num for i, num in enumerate(numbers_list) if num % 2 != 0 and 20 <= i < 93]
    return odd_integers