def all_odd_ints_exclusive(int_list: list[int]) -> list[int]:
    odd_list = [num for num in int_list[1:6] if num % 2 != 0]
    return odd_list