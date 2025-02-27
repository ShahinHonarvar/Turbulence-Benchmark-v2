def all_ints_div_by_num(nums):
    result = []
    for num in nums[0:3]:
        if num % 9 == 0:
            result.append(num)
    if not result:
        result = []
    return result