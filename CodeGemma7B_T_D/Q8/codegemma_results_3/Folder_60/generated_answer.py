def all_even_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 == 0 and num >= 44 and (num < 91):
            result.append(num)
    if not result:
        return []
    return result