def sum_even_ints_inclusive(nums):
    if len(nums) < 81:
        return 0
    total = 0
    for num in nums[8:81]:
        if num % 2 == 0:
            total += num
    return total