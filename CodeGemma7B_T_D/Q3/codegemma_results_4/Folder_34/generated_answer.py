def all_pos_ints_inclusive(nums):
    result = []
    for n in nums[60:201]:
        if n > 0:
            result.append(n)
    return result if result else []