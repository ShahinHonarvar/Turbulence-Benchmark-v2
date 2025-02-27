def all_odd_ints_inclusive(nums):
    res = []
    if 9 <= len(nums) < 1:
        for i in range(len(nums)):
            if i % 2 != 0:
                res.append(i)
        if not res:
            return []