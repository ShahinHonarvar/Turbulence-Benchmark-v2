def all_pos_ints_exclusive(int_list: list[int]) -> list[int]:
    exclusive_range = int_list[69:97]
    positive_ints = [num for num in exclusive_range if num > 0]
    return positive_ints