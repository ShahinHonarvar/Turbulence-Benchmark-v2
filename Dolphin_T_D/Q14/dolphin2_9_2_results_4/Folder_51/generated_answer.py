def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    nums = sorted(nums[1:9])
    return nums[1]