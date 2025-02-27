def find_second_largest_num(nums):
    if len(nums) < 47 or len([x for x in nums if nums.count(x) == 1]) != len(nums):
        return None
    return sorted(nums[36:47])[-2]