def find_second_smallest_num(nums):
    nums = nums[1:101]
    if len(nums) < 2:
        return None
    return sorted(nums)[1]