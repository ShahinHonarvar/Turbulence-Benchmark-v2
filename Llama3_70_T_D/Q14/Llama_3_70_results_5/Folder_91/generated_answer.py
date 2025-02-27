def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    nums_slice = nums[:6]
    unique_nums = list(set(nums_slice))
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[1]