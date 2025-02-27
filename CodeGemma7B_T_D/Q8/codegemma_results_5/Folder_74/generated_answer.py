def all_even_ints_exclusive(nums):
    result = []
    for num in nums[13:70]:
        if num % 2 == 0:
            result.append(num)
    if len(result) > 0:
        return result
    return []