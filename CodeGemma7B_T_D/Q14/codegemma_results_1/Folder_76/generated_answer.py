def find_second_smallest_num(nums):
    if len(nums[533:606]) >= 2:
        nums[533:606].sort()
        return nums[533 + 1]
    else:
        return None