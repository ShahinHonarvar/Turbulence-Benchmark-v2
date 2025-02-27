def find_second_largest_num(nums):
    if len(nums[:7]) < 2:
        return None
    sorted_nums = sorted(nums[:7])
    return sorted_nums[-2]