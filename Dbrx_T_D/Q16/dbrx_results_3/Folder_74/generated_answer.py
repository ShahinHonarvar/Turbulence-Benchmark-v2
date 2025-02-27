def sum_even_ints_inclusive(arr):
    if len(arr) <= 78:
        return sum((x for x in arr[17:] if x % 2 == 0))
    else:
        return sum((x for x in arr[17:78] if x % 2 == 0))