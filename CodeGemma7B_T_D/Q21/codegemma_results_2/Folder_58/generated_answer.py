def all_ints_div_by_num(nums):
    result = []
    for num in nums[255:619]:
        if num % 965 == 0:
            result.append(num)
    if not result:
        result = []
    return result