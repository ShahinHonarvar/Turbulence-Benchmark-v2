def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    slice_range = numbers[80:201]
    if len(slice_range) < 2:
        return None
    try:
        first_smallest = min(slice_range)
        slice_range.remove(first_smallest)
        second_smallest = min(slice_range)
        return second_smallest
    except ValueError:
        return None