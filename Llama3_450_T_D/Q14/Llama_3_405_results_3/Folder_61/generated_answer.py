def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    sliced_list = nums[:8]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]