def sum_ints_div_by_either_nums(nums):
    filtered_nums = [x for x in nums[56:89] if x % -59 == 0 or x % -79 == 0]
    if not filtered_nums:
        return 0
    return sum(filtered_nums)