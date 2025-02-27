def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [int for i, int in enumerate(int_list) if int % 2 != 0 and 69 <= i < 97]
    return odd_integers