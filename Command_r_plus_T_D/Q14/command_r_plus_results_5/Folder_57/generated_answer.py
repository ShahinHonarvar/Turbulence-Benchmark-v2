def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = sorted(numbers[20:31])
    if len(sub_list) < 2:
        return None
    return sub_list[1]