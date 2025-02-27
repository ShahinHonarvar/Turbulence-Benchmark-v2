def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sub_list = nums[62:100]
    if len(sub_list) < 2:
        return None
    largest = max(sub_list)
    sub_list.remove(largest)
    second_largest = max(sub_list)
    return second_largest