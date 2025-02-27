def all_even_ints_exclusive(arr):
    if len(arr) < 92 or len(arr) > 100:
        return []
    return [num for num in arr[56:92] if num % 2 == 0]