def sum_odd_ints_inclusive(nums):
    total = 0
    nums = nums[36:47]
    for num in nums:
        if num % 2 != 0:
            total += num
    if total == 0:
        return 0
    else:
        return total