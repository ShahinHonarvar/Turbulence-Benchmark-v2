def find_second_smallest_num(lst):
    sub_lst = [num for index, num in enumerate(lst) if 10 <= index <= 66]
    if len(sub_lst) < 2:
        return None
    sub_lst.sort()
    return sub_lst[1]