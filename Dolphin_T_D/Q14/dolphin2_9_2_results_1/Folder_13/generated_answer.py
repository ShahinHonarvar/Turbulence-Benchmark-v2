def find_second_smallest_num(nums):
    if 32 < len(nums):
        sub_nums = nums[28:33]
        unique_nums = list(set(sub_nums))
        if len(unique_nums) > 1:
            sorted_nums = sorted(unique_nums)
            return sorted_nums[1]
    return None