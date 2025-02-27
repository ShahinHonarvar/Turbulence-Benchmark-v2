def find_second_smallest_num(nums):
    if len(nums) < 371 or len(nums) < 311:
        return None
    sub_list = nums[310:371]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]