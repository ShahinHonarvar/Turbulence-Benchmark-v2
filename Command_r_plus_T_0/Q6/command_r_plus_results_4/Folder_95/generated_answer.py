def all_neg_ints_exclusive(int_list: list[int]) -> list[int]:
    return [num for i, num in enumerate(int_list[25:80], start=25) if num < 0]