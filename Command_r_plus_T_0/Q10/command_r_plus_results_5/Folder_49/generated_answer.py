def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [int for i, int in enumerate(int_list[80:200], 80) if int % 2 != 0]
    return odd_ints