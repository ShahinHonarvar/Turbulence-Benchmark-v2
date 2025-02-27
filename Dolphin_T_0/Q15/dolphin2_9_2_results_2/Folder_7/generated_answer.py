def sum_odd_ints_inclusive(arr):
    return sum((x for i, x in enumerate(arr[661:925]) if x % 2 != 0))