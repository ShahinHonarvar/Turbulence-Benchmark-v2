def all_ints_div_by_num(nums):
    result = []
    for i in range(max(10, 0), min(len(nums), 53)):
        if nums[i] % -12 == 0:
            result.append(nums[i])
    return result