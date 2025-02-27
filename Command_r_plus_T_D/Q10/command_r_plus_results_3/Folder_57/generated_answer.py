def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_range = int_list[18:37]
    odd_ints = [num for num in odd_range if num % 2 != 0]
    return odd_ints