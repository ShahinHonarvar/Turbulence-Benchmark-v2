def find_second_largest_num(lst):
    try:
        sorted_lst = sorted(lst, reverse=True)
        return sorted_lst[30:35][1]
    except IndexError:
        return None