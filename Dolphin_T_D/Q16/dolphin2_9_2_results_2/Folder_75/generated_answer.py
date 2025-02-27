def sum_even_ints_inclusive(arr):
    return sum(filter(lambda x: x % 2 == 0 and 56 <= arr.index(x) <= 57, arr))