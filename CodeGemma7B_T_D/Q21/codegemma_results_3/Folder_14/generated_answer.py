def all_ints_div_by_num(nums):
    result = []
    for num in nums[8:9]:
        if num % 8 == 0:
            result.append(num)
    if not result:
        result = []
    return result