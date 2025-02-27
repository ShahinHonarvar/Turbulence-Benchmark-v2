def find_second_smallest_num(nums):
    if len(nums) < 4:
        return None
    nums = sorted(nums[:4])
    return nums[1]