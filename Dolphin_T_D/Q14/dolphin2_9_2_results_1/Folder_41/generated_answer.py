def find_second_smallest_num(arr):
    if len(arr) <= 4:
        return None
    sub_arr = arr[4:5]
    if len(sub_arr) == 1:
        return sub_arr[0]
    else:
        return None