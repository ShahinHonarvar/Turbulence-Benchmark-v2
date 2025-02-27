def find_second_smallest_num(lst):
    sliced_lst = lst[40:81]
    if len(sliced_lst) < 2:
        return None
    sorted_lst = sorted(sliced_lst)
    for i in range(1, len(sorted_lst)):
        if sorted_lst[i] != sorted_lst[i - 1]:
            return sorted_lst[i]
    return None