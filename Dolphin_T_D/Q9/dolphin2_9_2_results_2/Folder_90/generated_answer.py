def all_odd_ints_inclusive(arr):
    output = [num for i, num in enumerate(arr[262:747]) if num % 2 != 0]
    return output