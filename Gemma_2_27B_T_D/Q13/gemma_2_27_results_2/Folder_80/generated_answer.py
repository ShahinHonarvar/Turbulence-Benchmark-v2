def find_second_largest_num(nums):
    if len(nums) < 66 or 64 >= len(nums):
        return None
    sub_list = nums[64:67]
    return sorted(sub_list)[-2]