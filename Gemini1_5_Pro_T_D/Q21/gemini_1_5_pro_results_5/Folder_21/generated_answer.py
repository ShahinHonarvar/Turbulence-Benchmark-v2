def all_ints_div_by_num(nums):
    result = []
    for i in range(max(572, 0), min(len(nums), 807)):
        if nums[i] % -158 == 0:
            result.append(nums[i])
    return result