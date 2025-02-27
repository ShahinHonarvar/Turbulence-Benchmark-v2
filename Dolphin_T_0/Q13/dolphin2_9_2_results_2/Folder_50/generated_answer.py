def find_second_largest_num(arr):
    if len(arr) < 2 or len(arr) > 85:
        return None
    else:
        sub_arr = arr[70:85]
        if len(sub_arr) < 2:
            return None
        else:
            max_val = max(sub_arr)
            sub_arr.remove(max_val)
            second_max_val = max(sub_arr)
            for index in range(len(sub_arr)):
                if sub_arr[index] == second_max_val:
                    return second_max_val
            return None