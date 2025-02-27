def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = numbers[20:31]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[-2]