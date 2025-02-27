def all_ints_div_by_num(nums):
    result = []
    for num in nums[30:60]:
        if num % 39 == 0:
            result.append(num)
    return result