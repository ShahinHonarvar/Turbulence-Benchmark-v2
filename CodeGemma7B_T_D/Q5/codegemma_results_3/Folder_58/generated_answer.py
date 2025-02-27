def all_neg_ints_inclusive(nums):
    for num in nums[209:557]:
        if num < 0:
            result.append(num)
    return result or []