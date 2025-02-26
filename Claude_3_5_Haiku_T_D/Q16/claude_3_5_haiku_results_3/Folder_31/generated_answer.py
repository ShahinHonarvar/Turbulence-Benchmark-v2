def sum_even_ints_inclusive(nums):
    if len(nums) <= 88:
        return 0
    total = 0
    for num in nums[75:89]:
        if num % 2 == 0:
            total += num
    return total