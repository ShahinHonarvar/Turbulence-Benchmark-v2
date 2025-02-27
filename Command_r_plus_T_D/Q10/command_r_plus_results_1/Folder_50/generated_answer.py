def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_ints = [num for num in int_list[70:98] if num % 2 != 0]
    return odd_ints