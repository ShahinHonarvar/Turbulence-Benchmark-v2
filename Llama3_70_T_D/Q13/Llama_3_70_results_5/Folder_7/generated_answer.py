def find_second_largest_num(lst):
    try:
        return sorted(lst[660:924])[::-1][1]
    except IndexError:
        return None