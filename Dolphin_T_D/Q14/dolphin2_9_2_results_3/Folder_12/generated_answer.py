def find_second_smallest_num(arr):
    if not arr:
        return None
    sub_arr = arr[31:73]
    if len(sub_arr) < 2:
        return None
    min1 = min(sub_arr)
    sub_arr.remove(min1)
    if not sub_arr:
        return None
    return min(sub_arr)