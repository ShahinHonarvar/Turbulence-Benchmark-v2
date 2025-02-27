def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[29:53]:
        if num % -68 != 0:
            result.append(num)
    return result