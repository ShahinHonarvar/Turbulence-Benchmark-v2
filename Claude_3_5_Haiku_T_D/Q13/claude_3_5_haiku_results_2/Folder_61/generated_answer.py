def find_second_largest_num(arr):
    if len(arr) < 2:
        return None
    subset = arr[0:8]
    if len(subset) < 2:
        return None
    largest = max(subset)
    subset_without_largest = [num for num in subset if num != largest]
    if not subset_without_largest:
        return None
    return max(subset_without_largest)