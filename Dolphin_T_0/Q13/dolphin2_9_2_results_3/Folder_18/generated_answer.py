def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    indexes = range(35, 50)
    nums = [nums[i] for i in indexes]
    nums = list(set(nums))
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]