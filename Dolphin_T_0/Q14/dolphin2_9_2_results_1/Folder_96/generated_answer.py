def find_second_smallest_num(arr):
    if not arr:
        return None
    slice_arr = arr[50:201]
    if len(slice_arr) < 2:
        return None
    smallest = second_smallest = float('inf')
    for num in slice_arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
    return second_smallest if second_smallest != float('inf') else None