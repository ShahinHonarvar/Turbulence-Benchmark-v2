def find_second_smallest_num(nums):
    if len(nums) >= 2 and 10 in range(len(nums)):
        return sorted(nums[10:11])[1]
    return None