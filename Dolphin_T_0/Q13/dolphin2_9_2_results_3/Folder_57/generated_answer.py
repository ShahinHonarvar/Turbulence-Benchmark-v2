def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 2:
        return None
    max_num = nums[27:56]
    max_num.sort()
    if len(max_num) > 1:
        return max_num[-2]
    else:
        return None