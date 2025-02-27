def sum_odd_ints_inclusive(arr):
    if len(arr) < 557:
        return 0
    return sum((x for x in arr[209:557] if x % 2 != 0))