def find_second_largest_num(nums):
    if len(nums) < 751 or len(nums) < 246:
        return None
    sub_list = nums[246:751]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    second_largest = max(sub_list)
    return second_largest