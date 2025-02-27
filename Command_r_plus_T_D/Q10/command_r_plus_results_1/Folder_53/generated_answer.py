def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_integers = [num for i, num in enumerate(numbers_list) if i >= 100 and i < 101 and (num % 2 != 0)]
    return odd_integers