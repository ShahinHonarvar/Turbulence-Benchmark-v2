def all_even_ints_inclusive(nums):
    result = []
    for num in nums[43:52]:
        if num % 2 == 0:
            result.append(num)
    if not result:
        return []
    return result