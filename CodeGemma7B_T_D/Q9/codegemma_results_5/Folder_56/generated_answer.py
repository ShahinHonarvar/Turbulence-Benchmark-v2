def all_odd_ints_inclusive(nums):
    if not any((num % 2 for num in nums)):
        return []
    result = []
    for num in nums:
        if num % 2:
            result.append(num)
    return result