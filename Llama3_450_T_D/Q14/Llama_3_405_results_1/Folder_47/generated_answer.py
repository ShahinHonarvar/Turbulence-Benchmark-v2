def find_second_smallest_num(nums):
    if len(nums) < 64:
        return None
    sliced_nums = nums[22:64]
    distinct_nums = list(set(sliced_nums))
    if len(distinct_nums) < 2:
        return None
    return sorted(distinct_nums)[1]