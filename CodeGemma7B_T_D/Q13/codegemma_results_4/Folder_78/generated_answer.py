def find_second_largest_num(nums):
    if len(nums) <= 1:
        return None
    nums = sorted(nums)[43:52]
    if len(nums) <= 1:
        return None
    return nums[-2]