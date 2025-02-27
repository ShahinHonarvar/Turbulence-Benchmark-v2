def find_second_largest_num(nums):
    new_nums = nums[55:99]
    if len(new_nums) < 2:
        return None
    elif len(set(new_nums)) < 2:
        return None
    else:
        new_nums.sort(reverse=True)
        return new_nums[1]