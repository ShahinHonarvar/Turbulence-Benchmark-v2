def all_odd_ints_exclusive(nums):
    odds = []
    for num in nums:
        if num % 2 != 0:
            if len(odds) < 8:
                odds.append(num)
    return odds