def find_second_smallest_num(arr):
    if len(arr) > 200:
        indices = arr[60:201]
        if len(indices) > 1:
            sorted_indices = sorted(indices)
            return sorted_indices[1]
    return None