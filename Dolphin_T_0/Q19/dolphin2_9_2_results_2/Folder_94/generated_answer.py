def all_ints_not_div_by_num(arr):
    start_index = 24
    end_index = 45
    new_arr = [num for num in arr[start_index:end_index] if num % -72 != 0]
    return new_arr if new_arr else []