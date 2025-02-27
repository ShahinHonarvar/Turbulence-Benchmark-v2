def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[33:78]:
        if num % -17 != 0:
            result.append(num)
    return result