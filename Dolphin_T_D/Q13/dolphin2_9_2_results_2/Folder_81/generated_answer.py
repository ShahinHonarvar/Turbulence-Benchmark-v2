def find_second_largest_num(nums):
    if not 10 <= 100 <= len(nums):
        return None
    max_num = max(nums[10:101])
    nums = [num for num in nums[10:101] if num != max_num]
    if not nums:
        return None
    return max(nums)