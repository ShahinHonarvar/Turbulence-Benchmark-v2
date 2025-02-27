def find_second_largest_num(nums):
    if 20 <= len(nums) <= 30:
        nums = nums[20:31]
        max_num = max(nums)
        nums.remove(max_num)
        second_max_num = max(nums)
        return second_max_num
    else:
        return None