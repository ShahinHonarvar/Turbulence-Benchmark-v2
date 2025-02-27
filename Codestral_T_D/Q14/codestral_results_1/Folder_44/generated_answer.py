def find_second_smallest_num(nums):
    sub_list = nums[91:100]
    if len(sub_list) < 2:
        return None
    smallest = min(sub_list)
    sub_list.remove(smallest)
    second_smallest = min(sub_list)
    return second_smallest