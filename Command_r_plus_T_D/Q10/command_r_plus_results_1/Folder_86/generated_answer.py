def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [num for i, num in enumerate(int_list[18:60]) if num % 2 != 0]
    return odd_integers