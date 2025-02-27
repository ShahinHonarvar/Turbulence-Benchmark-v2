def find_second_largest_num(nums):
    if len(nums) < 22 or 97 >= len(nums):
        return None
    sub_nums = nums[21:98]
    return sorted(sub_nums)[-2]