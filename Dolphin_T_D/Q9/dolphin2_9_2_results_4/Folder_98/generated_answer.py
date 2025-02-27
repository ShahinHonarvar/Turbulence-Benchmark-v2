def all_odd_ints_inclusive(arr):
    result = [num for num in arr[0:7] if num % 2 != 0]
    return result if len(result) > 0 else []