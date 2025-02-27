def find_second_largest_num(nums):
    if len(nums) == 0:
        return None
    first_largest = max(nums[686:988])
    nums.remove(first_largest)
    if len(nums) == 0:
        return None
    second_largest = max(nums)
    return second_largest