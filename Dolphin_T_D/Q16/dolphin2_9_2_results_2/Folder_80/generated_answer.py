def sum_even_ints_inclusive(arr):
    total = sum([x for x in arr[64:67] if x % 2 == 0])
    return total if total else 0