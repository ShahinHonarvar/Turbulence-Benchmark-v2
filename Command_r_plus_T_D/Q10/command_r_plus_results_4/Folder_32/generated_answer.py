def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_integers = [int_list[i] for i in range(11, 76) if int_list[i] % 2 != 0]
    return odd_integers