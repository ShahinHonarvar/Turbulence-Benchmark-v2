def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[58:76]:
        if num % 72 == 0 and num % 62 == 0:
            result.append(num)
    return result