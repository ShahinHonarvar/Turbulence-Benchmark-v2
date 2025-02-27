def find_second_smallest_num(nums):
    if len(nums) < 50:
        return None
    sub_list = nums[22:51]
    unique_nums = list(set(sub_list))
    unique_nums.sort()
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]