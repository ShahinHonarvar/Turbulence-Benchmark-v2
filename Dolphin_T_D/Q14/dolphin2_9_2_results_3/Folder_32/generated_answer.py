def find_second_smallest_num(nums):
    try:
        nums_slice = nums[32:36]
        nums_sorted = sorted(nums_slice)
        second_smallest = nums_sorted[1]
        return second_smallest
    except (IndexError, ValueError):
        return None