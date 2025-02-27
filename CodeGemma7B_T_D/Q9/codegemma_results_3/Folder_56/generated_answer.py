def all_odd_ints_inclusive(nums):
    result = []
    for num in nums:
        if num % 2 != 0:
            result.append(num)
    return result if result else []