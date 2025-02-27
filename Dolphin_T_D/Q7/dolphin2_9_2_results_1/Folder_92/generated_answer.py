def all_even_ints_inclusive(arr):
    result = [num for num in arr[0:2] if num % 2 == 0]
    return result if result else []