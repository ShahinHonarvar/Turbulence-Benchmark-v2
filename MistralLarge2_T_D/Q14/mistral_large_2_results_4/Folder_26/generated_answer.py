def find_second_smallest_num(nums):
    if len(nums) <= 78:
        return None
    sub_list = nums[62:79]
    if len(sub_list) < 2:
        return None
    first_smallest = min(sub_list)
    sub_list.remove(first_smallest)
    second_smallest = min(sub_list)
    return second_smallest