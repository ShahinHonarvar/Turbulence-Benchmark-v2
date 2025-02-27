def find_second_largest_num(nums):
    if len(nums) < 2 or len(nums) > 5:
        return None
    sorted_nums = sorted(nums[:5])
    return sorted_nums[-2]