def find_second_smallest_num(numbers):
    nums_in_range = sorted(numbers[70:201])
    if len(nums_in_range) < 2:
        return None
    return nums_in_range[1]