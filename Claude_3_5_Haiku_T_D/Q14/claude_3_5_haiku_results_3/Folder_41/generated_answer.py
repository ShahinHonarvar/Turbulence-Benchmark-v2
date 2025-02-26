def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    slice_nums = numbers[4:5]
    if not slice_nums:
        return None
    return slice_nums[0]