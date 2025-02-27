def find_second_smallest_num(nums):
    try:
        nums = sorted(nums[22:89])
        return nums[1]
    except IndexError:
        return None