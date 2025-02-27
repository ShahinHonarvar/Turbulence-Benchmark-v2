def all_pos_ints_exclusive(nums):
    result = []
    for num in nums[20:35]:
        if num > 0 and num not in result:
            result.append(num)
    return result