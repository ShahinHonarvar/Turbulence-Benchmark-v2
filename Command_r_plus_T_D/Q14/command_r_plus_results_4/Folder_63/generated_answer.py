def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sub_list = numbers[56:83]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]