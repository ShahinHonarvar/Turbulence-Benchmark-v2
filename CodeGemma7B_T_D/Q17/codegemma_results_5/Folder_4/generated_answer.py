def all_ints_div_by_both_two_nums(nums):
    if not nums:
        return []
    result = []
    for num in nums[86:91]:
        if num % -71 == 0 and num % -67 == 0:
            result.append(num)
    return result