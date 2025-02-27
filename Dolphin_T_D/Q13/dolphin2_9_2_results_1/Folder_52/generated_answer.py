def find_second_largest_num(nums):
    if 28 <= len(nums) <= 38:
        new_nums = nums[28:38]
        if len(set(new_nums)) < 2:
            return 'None'
        else:
            first_max = max(new_nums)
            new_nums.remove(first_max)
            return max(new_nums)
    else:
        return 'None'