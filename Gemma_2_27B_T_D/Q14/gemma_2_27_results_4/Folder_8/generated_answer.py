def find_second_smallest_num(nums):
    if len(nums) < 66 or len(nums) < 56:
        return None
    sub_list = nums[56:67]
    sorted_list = sorted(sub_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]