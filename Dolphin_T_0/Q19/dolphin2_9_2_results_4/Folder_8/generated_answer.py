def all_ints_not_div_by_num(nums):
    result = []
    for num in nums:
        if num % -75 != 0 and 17 < nums.index(num) < 88:
            result.append(num)
    return result