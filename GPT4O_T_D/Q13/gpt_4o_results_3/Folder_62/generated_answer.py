def find_second_largest_num(nums):
    if len(nums) < 100:
        return None
    sub_list = nums[91:100]
    unique_nums = list(set(sub_list))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]