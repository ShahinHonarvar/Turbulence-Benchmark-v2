def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = numbers[43:52]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]