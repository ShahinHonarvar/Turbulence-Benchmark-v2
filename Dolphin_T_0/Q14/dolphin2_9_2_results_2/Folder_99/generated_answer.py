def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    start_index = 608
    end_index = 609
    if start_index < 0 or end_index >= len(nums):
        return None
    sublist = nums[start_index:end_index + 1]
    if len(sublist) < 2:
        return None
    sorted_list = sorted(sublist)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]