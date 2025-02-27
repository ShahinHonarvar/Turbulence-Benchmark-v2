def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 5:
        return None
    else:
        new_nums = sorted(nums[0:5])
        return new_nums[len(new_nums) - 2]