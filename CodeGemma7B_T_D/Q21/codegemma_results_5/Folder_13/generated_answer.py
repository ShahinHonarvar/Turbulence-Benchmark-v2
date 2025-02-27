def all_ints_div_by_num(nums):
    result = []
    for num in nums[36:41]:
        if num % 28 == 0:
            result.append(num)
    return result