def find_second_smallest_num(list):
    if not list:
        return None
    list = sorted(list[52:72])
    return list[1] if len(list) > 1 else None