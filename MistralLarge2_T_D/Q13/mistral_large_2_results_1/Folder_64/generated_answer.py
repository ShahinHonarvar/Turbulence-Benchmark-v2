def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    distinct_nums = list(set(nums[:5]))
    if len(distinct_nums) < 2:
        return None
    distinct_nums.sort(reverse=True)
    return distinct_nums[1]