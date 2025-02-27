def all_odd_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 != 0 and 20 < num < 43:
            result.append(num)
    return result