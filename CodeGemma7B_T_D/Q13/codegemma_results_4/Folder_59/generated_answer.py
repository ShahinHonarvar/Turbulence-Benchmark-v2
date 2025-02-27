def find_second_largest_num(list):
    list.sort()
    if len(list) >= 10:
        return list[-2]
    else:
        return 'None'