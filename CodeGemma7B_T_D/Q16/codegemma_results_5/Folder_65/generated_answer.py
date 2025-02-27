def sum_even_ints_inclusive(nums):
    res = 0
    for num in nums[56:99]:
        if num % 2 == 0:
            res += num
    return res or 0