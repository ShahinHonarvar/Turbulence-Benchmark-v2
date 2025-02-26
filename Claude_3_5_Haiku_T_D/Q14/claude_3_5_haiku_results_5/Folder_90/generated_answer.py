def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 540:
        return None
    slice_nums = numbers[527:539]
    if len(slice_nums) < 2:
        return None
    sorted_slice = sorted(slice_nums)
    return sorted_slice[1]