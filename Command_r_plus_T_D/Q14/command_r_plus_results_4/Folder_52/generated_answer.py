def find_second_smallest_num(numbers_list: list[int]) -> int:
    if len(numbers_list) < 67:
        return None
    sub_list = numbers_list[64:67]
    sub_list.sort()
    return sub_list[1] if len(sub_list) > 1 else None