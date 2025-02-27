def all_ints_not_div_by_num(arr):
    result = [i for i in arr[15:63] if i % 34 != 0]
    return result if len(result) > 0 else []