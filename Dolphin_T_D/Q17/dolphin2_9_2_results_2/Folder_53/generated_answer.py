def all_ints_div_by_both_two_nums(nums):
    result = []
    for i in nums[200:201]:
        if i % 17 == 0 and i % -5 == 0:
            result.append(i)
    return result