def find_second_smallest_num(nums):
    if len(nums) < 55 or 34 < len(nums) - 55:
        return 'None'
    sub_list = nums[34:56]
    return sorted(sub_list)[1]