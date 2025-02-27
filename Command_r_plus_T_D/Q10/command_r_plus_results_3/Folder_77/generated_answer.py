def all_odd_ints_exclusive(numbers_list: list[int]) -> list[int]:
    odd_integers = [num for i, num in enumerate(numbers_list) if i > 110 and i < 473 and (num % 2 != 0)]
    return odd_integers