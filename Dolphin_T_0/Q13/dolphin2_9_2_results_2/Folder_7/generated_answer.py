def find_second_largest_num(nums):
    if 924 < len(nums) < 661:
        return None
    else:
        sliced_nums = nums[661:925]
        if len(sliced_nums) < 2:
            return None
        else:
            max_num = max(sliced_nums)
            sliced_nums.remove(max_num)
            second_max_num = max(sliced_nums)
            return second_max_num