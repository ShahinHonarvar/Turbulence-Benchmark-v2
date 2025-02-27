def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    start = min(nums[0], nums[1])
    end = max(nums[0], nums[1])
    return [i for i in range(start, end + 1) if i % 2 == 0 and i % 1 == 0]