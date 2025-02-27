def find_second_smallest_num(list):
    if len(list) < 57 or len(list) > 99:
        return None
    list.sort()
    return list[56] if list[56] == list[57] else list[57]