def find_second_largest_num(lst):
    if len(lst) < 5 or len(lst) > 9:
        return 'None'
    return sorted(lst[4:9], reverse=True)[1]