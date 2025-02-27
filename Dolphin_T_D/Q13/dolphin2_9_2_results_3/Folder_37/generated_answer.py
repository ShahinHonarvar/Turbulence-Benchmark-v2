def find_second_largest_num(arr):
    sub_arr = arr[1:5]
    if len(set(sub_arr)) < 2:
        return None
    sub_arr.sort(reverse=True)
    return sub_arr[1]