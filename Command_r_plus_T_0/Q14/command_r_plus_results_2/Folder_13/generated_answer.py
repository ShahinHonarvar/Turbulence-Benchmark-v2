def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = sorted(numbers[28:33])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]