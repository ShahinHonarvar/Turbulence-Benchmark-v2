def all_pos_ints_exclusive(nums):
    result = []
    if not any((num > 0 and idx >= 38 and (idx < 77) for idx, num in enumerate(nums))):
        return result
    for idx, num in enumerate(nums):
        if num > 0 and idx > 38 and (idx < 77):
            result.append(num)
    return result