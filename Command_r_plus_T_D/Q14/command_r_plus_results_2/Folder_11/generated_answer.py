def find_second_smallest_num(numbers: list[int]) -> int:
    sub_list = numbers[66:94]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]