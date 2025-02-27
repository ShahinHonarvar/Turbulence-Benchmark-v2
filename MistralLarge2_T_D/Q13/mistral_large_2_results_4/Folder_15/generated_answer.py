def find_second_largest_num(nums):
    if len(nums) < 4:
        return None
    sorted_nums = sorted(nums[:4])
    return sorted_nums[-2]