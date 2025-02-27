def sum_odd_ints_inclusive(nums):
    total = 0
    for num in nums[29:80]:
        if num % 2 != 0:
            total += num
    return total if total else 0