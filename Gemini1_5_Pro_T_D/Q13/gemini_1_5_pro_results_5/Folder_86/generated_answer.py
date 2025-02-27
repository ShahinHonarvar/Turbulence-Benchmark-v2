def find_second_largest_num(nums):
    sub_nums = nums[31:35]
    if len(sub_nums) < 2:
        return None
    largest_num = max(sub_nums)
    sub_nums.remove(largest_num)
    if len(sub_nums) == 0:
        return None
    return max(sub_nums)