def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 64:
        return None
    else:
        numbers_list_subset = numbers_list[62:64]
        numbers_list_subset.sort()
        return numbers_list_subset[1]