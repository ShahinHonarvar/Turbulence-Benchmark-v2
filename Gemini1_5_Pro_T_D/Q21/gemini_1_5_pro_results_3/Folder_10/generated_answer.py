def all_ints_div_by_num(nums):
    result = []
    for i in range(max(0, 42), min(len(nums), 90)):
        if nums[i] % -59 == 0:
            result.append(nums[i])
    return result