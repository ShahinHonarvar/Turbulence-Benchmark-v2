def find_second_smallest_num(nums):
    if 25 <= len(nums) <= 87:
        sub_list = nums[25:88]
        sub_list.sort()
        if len(sub_list) >= 2:
            return sub_list[1]
    return None