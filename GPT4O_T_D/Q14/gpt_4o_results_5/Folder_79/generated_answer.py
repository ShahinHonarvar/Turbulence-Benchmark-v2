def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    sub_list = nums[1:6]
    unique_nums = list(set(sub_list))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[1]