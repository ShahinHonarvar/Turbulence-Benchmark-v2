def find_second_smallest_num(nums):
    if len(nums) < 99 or len(nums) < 92:
        return None
    sub_list = nums[91:100]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]