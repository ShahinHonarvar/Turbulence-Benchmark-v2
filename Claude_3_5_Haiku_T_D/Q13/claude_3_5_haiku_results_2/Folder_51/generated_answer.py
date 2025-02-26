def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    slice_nums = numbers[1:9]
    if len(set(slice_nums)) < 2:
        return None
    sorted_slice = sorted(slice_nums, reverse=True)
    return sorted_slice[1]