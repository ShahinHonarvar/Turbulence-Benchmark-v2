def find_second_smallest_num(nums):
    sub_nums = nums[90:100]
    if len(sub_nums) < 2:
        return None
    sub_nums = list(set(sub_nums))
    sub_nums.sort()
    if len(sub_nums) < 2:
        return None
    return sub_nums[1]