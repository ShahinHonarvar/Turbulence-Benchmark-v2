def sum_even_ints_inclusive(arr):
    return sum((val for val in arr[30:201] if val % 2 == 0))