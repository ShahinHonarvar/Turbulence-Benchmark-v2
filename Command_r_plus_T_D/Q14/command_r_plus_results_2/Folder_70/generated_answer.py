def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = sorted(numbers[35:50])
    if len(sub_list) > 1:
        return sub_list[1]
    return None