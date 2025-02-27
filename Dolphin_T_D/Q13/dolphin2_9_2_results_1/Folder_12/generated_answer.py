def find_second_largest_num(arr):
    if len(arr) < 2:
        return None
    lst = arr[14:65]
    max_num = max(lst)
    lst.remove(max_num)
    if len(lst) < 2:
        return None
    second_max_num = max(lst)
    return second_max_num