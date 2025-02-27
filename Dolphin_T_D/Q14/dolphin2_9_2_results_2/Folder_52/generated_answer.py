def find_second_smallest_num(nums):
    if len(nums) < 2 or not all((isinstance(i, (int, float)) for i in nums)):
        return 'None'
    min_ = min(nums[64:67])
    nums.remove(min_)
    if not nums or min_(nums[64:67]) == min_:
        return 'None'
    return min_(nums[64:67])