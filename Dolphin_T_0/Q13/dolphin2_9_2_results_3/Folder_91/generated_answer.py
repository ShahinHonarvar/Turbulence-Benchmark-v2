def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    max_num = max(nums[0:6])
    nums.remove(max_num)
    second_max_num = max(nums[0:6])
    return second_max_num