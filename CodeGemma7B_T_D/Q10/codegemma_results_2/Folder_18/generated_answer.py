def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    result = []
    for num in nums[57:84]:
        if num % 2 == 1:
            result.append(num)
    return result if result else []