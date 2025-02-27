def all_ints_div_by_num(arr):
    result = [i for i in arr[29:301] if i % 5 == 0]
    return result if result else []