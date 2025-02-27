def all_odd_ints_inclusive(nums):
    res = []
    for num in nums[70:85]:
        if num % 2 != 0:
            res.append(num)
    return res or []