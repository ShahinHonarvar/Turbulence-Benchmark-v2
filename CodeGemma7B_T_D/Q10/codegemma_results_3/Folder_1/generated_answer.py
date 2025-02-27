def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[66:90]:
        if num % 2 != 0:
            result.append(num)
    return result if len(result) > 0 else []