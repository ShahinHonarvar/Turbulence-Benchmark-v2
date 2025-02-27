def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[57:86]:
        if num % -77 == 0 and num % -32 == 0:
            result.append(num)
    if not result:
        return []
    return result