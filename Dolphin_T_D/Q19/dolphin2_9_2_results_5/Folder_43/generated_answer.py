def all_ints_not_div_by_num(arr):
    new_arr = arr[16:87]
    result = [num for num in new_arr if num % -15 != 0]
    return result