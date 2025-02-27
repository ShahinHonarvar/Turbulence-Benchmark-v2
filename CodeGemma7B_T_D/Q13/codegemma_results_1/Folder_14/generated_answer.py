def find_second_largest_num(nums):
    nums = nums[5:8]
    nums.remove(max(nums))
    if not nums:
        return None
    else:
        return max(nums)