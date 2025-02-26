def sum_odd_ints_inclusive(nums):
    if len(nums) < 42:
        return 0
    total = 0
    for num in nums[40:42]:
        if num % 2 != 0:
            total += num
    return total