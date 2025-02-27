def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[19:94]:
        if num % -32 != 0:
            result.append(num)
    return result