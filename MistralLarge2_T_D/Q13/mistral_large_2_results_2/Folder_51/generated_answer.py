def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    sub_list = nums[1:9]
    if len(sub_list) < 2:
        return None
    first_largest = max(sub_list)
    sub_list.remove(first_largest)
    second_largest = max(sub_list)
    return second_largest