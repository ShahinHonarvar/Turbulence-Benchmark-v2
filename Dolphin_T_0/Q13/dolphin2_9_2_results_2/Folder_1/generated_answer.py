def find_second_largest_num(arr):
    if 72 < len(arr) < 31:
        return None
    else:
        sub_arr = arr[31:73]
        if len(set(sub_arr)) < 2:
            return None
        else:
            sub_arr.sort(reverse=True)
            return sub_arr[1]