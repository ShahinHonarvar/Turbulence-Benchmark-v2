def find_second_smallest_num(lst):
    if len(lst) < 2:
        return None
    slice_lst = lst[70:201]
    smallest = min(slice_lst)
    second_smallest = min((i for i in slice_lst if i != smallest))
    return second_smallest if second_smallest != smallest else None