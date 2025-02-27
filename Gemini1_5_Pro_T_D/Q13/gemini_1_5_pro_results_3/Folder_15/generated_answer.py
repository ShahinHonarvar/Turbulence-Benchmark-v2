def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    sub_nums = nums[:4]
    sub_nums.sort()
    if len(sub_nums) == len(set(sub_nums)):
        return sub_nums[2]
    return None