def all_odd_ints_inclusive(nums):
    if not nums:
        return []
    result = []
    for num in nums:
        if num % 2 != 0 and 0 <= num <= 9:
            result.append(num)
    return result or []