def all_ints_div_by_num(arr):
    return [i for i in arr[13:64] if i % 46 == 0] if any((i % 46 == 0 for i in arr[13:64])) else []