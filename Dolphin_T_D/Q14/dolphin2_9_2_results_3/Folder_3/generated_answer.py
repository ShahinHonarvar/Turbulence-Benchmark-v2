def find_second_smallest_num(nums):
    if 55 < len(nums):
        sub_nums = nums[26:56]
        if len(sub_nums) > 1:
            sub_nums.sort()
            return sub_nums[1]
    return None