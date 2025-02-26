def find_second_smallest_num(numbers):
    if len(numbers) < 35:
        return None
    slice_nums = numbers[31:35]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(slice_nums)
    return sorted_slice[1]