def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[64:80]:
        if num % -95 != 0:
            result.append(num)
    return result