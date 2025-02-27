def find_second_smallest_num(nums):
    if len(nums) < 51 or 43 not in range(len(nums)):
        return None
    sub_list = nums[43:52]
    if len(sub_list) < 2:
        return None
    return sorted(sub_list)[1]