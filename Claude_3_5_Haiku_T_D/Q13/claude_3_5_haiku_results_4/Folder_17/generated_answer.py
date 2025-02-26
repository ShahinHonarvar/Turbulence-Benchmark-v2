def find_second_largest_num(numbers):
    if len(numbers) < 64 or len(numbers) <= 78:
        return None
    slice_nums = numbers[62:79]
    sorted_slice = sorted(slice_nums, reverse=True)
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]