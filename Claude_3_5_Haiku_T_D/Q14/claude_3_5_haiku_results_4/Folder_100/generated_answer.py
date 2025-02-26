def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    slice_nums = numbers[43:52]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(slice_nums)
    return sorted_slice[1]