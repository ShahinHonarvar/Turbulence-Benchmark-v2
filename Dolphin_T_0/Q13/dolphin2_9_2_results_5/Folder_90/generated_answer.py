def find_second_largest_num(arr):
    arr = arr[262:747]
    if len(arr) < 2:
        return None
    else:
        first, second = (None, None)
        for num in arr:
            if num > first:
                first, second = (num, first)
            elif num < first and num > second:
                second = num
        return second