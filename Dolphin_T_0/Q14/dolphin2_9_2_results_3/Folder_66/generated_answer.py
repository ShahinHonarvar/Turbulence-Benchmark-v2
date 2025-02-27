def find_second_smallest_num(nums):
    nums = nums[62:100]
    if len(nums) < 2:
        return None
    smallest = min(nums)
    nums = [num for num in nums if num != smallest]
    if not nums:
        return None
    return min(nums)