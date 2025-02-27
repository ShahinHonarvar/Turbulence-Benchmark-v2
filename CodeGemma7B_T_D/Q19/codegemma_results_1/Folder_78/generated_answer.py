def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[10:55]:
        if num % 36 != 0:
            result.append(num)
    return result