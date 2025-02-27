def all_odd_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 != 0:
            if num > 0:
                result.append(num)
    return result