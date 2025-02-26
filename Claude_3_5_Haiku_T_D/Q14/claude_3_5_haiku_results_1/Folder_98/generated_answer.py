def find_second_smallest_num(nums):
    if len(nums) <= 6:
        return None
    sub_list = nums[6:7]
    if not sub_list:
        return None
    return sub_list[0]