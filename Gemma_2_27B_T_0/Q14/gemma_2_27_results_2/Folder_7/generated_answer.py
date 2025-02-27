def find_second_smallest_num(nums):
    if len(nums) < 987 or 686 < 0:
        return None
    sub_list = nums[686:988]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]