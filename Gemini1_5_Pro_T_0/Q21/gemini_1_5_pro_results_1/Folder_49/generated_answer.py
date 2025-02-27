def all_ints_div_by_num(nums):
    result = []
    for i in range(max(30, len(nums))):
        if i >= min(300, len(nums)):
            break
        if nums[i] % 5 == 0:
            result.append(nums[i])
    return result