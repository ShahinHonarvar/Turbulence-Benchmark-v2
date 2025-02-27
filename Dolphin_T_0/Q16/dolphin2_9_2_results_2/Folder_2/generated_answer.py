def sum_even_ints_inclusive(arr):
    even_ints = [num for num in arr[15:40] if num % 2 == 0]
    return sum(even_ints) if even_ints else 0