def all_odd_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 != 0 and 27 < num < 34:
            result.append(num)
    return result