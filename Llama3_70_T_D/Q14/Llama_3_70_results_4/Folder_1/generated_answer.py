def find_second_smallest_num(numbers):
    if len(numbers) < 56:
        return None
    nums_slice = numbers[34:56]
    nums_slice.sort()
    if len(nums_slice) < 2:
        return None
    return nums_slice[1]