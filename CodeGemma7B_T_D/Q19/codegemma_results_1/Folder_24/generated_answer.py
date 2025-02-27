def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[41:69]:
        if num % -82 != 0:
            result.append(num)
    return result