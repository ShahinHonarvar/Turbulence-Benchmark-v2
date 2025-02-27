def find_second_largest_num(lst):
    try:
        return sorted(lst[91:100])[-2]
    except IndexError:
        return None