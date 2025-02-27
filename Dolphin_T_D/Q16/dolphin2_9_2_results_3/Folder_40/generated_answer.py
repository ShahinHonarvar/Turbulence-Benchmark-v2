def sum_even_ints_inclusive(arr):
    return sum((x for x in arr[0:3] if x % 2 == 0))