def find_second_largest_num(nums):
    if len(nums) < 55:
        return None
    else:
        sliced_nums = nums[50:55]
        if len(set(sliced_nums)) != len(sliced_nums):
            return None
        else:
            sorted_nums = sorted(sliced_nums)
            return sorted_nums[-2]