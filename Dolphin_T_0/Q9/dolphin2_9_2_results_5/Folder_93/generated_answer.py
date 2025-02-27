def all_odd_ints_inclusive(arr):
    odd_numbers = [num for index, num in enumerate(arr[75:95]) if num % 2 != 0]
    return odd_numbers