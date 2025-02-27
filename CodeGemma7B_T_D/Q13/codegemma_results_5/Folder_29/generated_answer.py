def find_second_largest_num(nums):
    nums = nums[59:98]
    if not nums:
        return None
    nums.sort(reverse=True)
    return nums[1]