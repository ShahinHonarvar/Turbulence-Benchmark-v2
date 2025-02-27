def find_second_largest_num(list):
    list = sorted(list)
    if len(list) >= 92:
        return list[len(list) - 2]
    else:
        return None