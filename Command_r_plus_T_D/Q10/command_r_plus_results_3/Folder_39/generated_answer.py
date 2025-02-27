def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [num for num in int_list[43:99] if num % 2 != 0]
    return odd_integers