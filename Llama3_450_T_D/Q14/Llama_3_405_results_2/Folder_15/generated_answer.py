def find_second_smallest_num(nums):
    if len(nums) < 2 or len(nums) > 5:
        return None
    sliced_nums = nums[:4]
    unique_nums = set(sliced_nums)
    if len(unique_nums) < 2:
        return None
    return sorted(unique_nums)[1]