def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 4:
        return None
    sub_nums = nums[:4]
    sub_nums.sort()
    return sub_nums[1] if len(sub_nums) > 1 and sub_nums[0] != sub_nums[1] else None