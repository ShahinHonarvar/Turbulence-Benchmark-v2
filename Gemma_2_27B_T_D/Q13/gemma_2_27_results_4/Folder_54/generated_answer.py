def find_second_largest_num(nums):
    if len(nums) < 55:
        return None
    sub_list = nums[34:56]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    return max(sub_list)