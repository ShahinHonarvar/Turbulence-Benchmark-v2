def find_second_smallest_num(lst):
    if len(lst) < 78:
        return None
    selected_nums = lst[66:78]
    selected_nums.sort()
    if len(selected_nums) < 2:
        return None
    return selected_nums[1]