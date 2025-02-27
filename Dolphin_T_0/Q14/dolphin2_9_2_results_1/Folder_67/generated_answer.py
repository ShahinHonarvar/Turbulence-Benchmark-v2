def find_second_smallest_num(nums):
    if 54 < len(nums):
        sub_nums = nums[50:55]
        if len(sub_nums) >= 2:
            min_num = min(sub_nums)
            sub_nums.remove(min_num)
            if len(sub_nums) >= 1:
                return min(sub_nums)
    return None