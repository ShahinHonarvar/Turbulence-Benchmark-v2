def find_second_largest_num(nums):
    if len(nums[:9]) < 2:
        return None
    sorted_nums = sorted(nums[:9])
    return sorted_nums[-2]