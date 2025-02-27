def find_second_smallest_num(nums):
    if len(nums) > 87:
        sub_list = nums[30:88]
        sub_list.sort()
        return sub_list[1] if len(sub_list) > 1 else None
    return None