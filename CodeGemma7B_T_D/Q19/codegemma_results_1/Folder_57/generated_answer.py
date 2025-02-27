def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[56:88]:
        if num % -59 != 0:
            result.append(num)
    return result