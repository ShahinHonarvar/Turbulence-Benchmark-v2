def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    else:
        new_list = nums[5:8]
        new_list.sort()
        return new_list[1]