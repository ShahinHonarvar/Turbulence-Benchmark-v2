def find_second_largest_num(numbers_list: list[int]) -> int:
    if not numbers_list:
        raise ValueError('Input list is empty.')
    if len(numbers_list) < 56:
        return None
    target_slice = numbers_list[34:56]
    target_slice.sort()
    if len(target_slice) < 2:
        return None
    return target_slice[-2]