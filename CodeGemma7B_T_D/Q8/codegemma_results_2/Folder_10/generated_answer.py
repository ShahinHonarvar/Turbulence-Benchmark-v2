def all_even_ints_exclusive(nums):
    result = []
    for n in nums:
        if n % 2 == 0 and 48 < n < 74:
            result.append(n)
    if not result:
        return []
    return result