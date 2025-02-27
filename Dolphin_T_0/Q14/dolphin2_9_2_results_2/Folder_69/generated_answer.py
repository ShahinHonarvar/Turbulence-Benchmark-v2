def find_second_smallest_num(lst):
    try:
        second_smallest_lst = sorted(lst[25:88])[1]
        return second_smallest_lst
    except:
        return None