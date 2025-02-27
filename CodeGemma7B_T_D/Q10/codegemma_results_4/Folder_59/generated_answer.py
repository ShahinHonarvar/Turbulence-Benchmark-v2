def all_odd_ints_exclusive(nums):
    result = []
    for num in nums:
        if num % 2 != 0 and num >= 0 and (num <= 9):
            result.append(num)
    return result