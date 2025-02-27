def sum_even_ints_inclusive(arr):
    return sum((num for num in arr[27:56:2] if num % 2 == 0))