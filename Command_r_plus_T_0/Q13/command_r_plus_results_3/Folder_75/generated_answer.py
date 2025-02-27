def find_second_largest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 58:
        return None
    else:
        numbers_slice = numbers_list[56:58]
        numbers_slice.sort()
        return numbers_slice[1] if len(numbers_slice) > 1 else None