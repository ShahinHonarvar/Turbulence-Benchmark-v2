def find_second_smallest_num(nums):
    if len(nums) < 66 or 56 < len(nums) - 1:
        return None
    sub_list = nums[56:67]
    sub_list.sort()
    return sub_list[1]