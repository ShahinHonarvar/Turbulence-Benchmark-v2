def all_odd_ints_exclusive(nums):
    result = []
    for num in nums[2:5]:
        if num % 2 != 0:
            result.append(num)
    if not result:
        return []
    return result