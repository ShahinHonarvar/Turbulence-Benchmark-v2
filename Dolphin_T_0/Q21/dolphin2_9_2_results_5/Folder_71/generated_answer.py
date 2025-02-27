def all_ints_div_by_num(arr):
    result = [num for num in arr[29:52] if num % -37 == 0]
    if not result:
        result = []
    return result