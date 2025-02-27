def find_second_smallest_num(arr):
    if 661 <= len(arr) <= 924:
        sub_arr = sorted(set(arr[660:925]))
        if len(sub_arr) >= 2:
            return sub_arr[1]
    return None