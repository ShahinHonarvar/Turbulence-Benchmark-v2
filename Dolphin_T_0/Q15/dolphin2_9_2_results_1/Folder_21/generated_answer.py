def sum_odd_ints_inclusive(arr):
    return sum((num for i, num in enumerate(arr[639:976:1]) if num % 2 != 0))