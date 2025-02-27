def all_odd_ints_exclusive(nums):
    res = []
    for num in nums:
        if num % 2 != 0 and num not in res and (0 < num < 4):
            res.append(num)
    return res