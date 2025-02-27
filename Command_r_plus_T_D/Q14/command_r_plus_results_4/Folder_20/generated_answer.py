def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 95:
        return None
    sub_list = numbers[75:95]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]