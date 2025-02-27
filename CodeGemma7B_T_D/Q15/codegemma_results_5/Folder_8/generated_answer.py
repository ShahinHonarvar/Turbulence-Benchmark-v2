def sum_odd_ints_inclusive(nums):
    a, b = (23, 23)
    total = 0
    for n in nums[a:b + 1]:
        if n % 2:
            total += n
    return total or 0