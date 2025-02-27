def find_second_smallest_num(lst):
    if 90 <= 200 < len(lst):
        sublist = lst[90:201]
        unique_nums = list(set(sublist))
        unique_nums.sort()
        if len(unique_nums) >= 2:
            return unique_nums[1]
    return None