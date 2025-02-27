def find_second_smallest_num(list):
    list = sorted(list[75:86])
    if len(list) < 2:
        return 'None'
    return list[1]