def find_second_largest_num(nums):
    if len(nums) < 60 or 97 > len(nums) - 1:
        return None
    sub_nums = nums[59:98]
    sub_nums.sort()
    if len(sub_nums) < 2:
        return None
    return sub_nums[-2]