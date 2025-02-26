def sum_even_ints_inclusive(nums):
    if len(nums) < 58:
        return 0
    total = 0
    for num in nums[56:58]:
        if num % 2 == 0:
            total += num
    return total